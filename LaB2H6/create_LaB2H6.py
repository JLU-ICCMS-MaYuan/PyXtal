# -*- coding: utf-8 -*-
"""
Bulk generator: La (2a) + B2H6 (4d) in I4/mmm-like groups
"""
import os
from pathlib import Path
from numpy import random
from pymatgen.core.structure import Molecule
from pyxtal import pyxtal
from pyxtal.molecule import pyxtal_molecule
from typing import Tuple, Optional


def generate_structures(n_struct: int,
                        out_dir: str = ".",
                        prefix: str = "LaB2H6",
                        group_range: Tuple = list(range(1, 230)),
                        factor: float = 2.0,
                        max_trials: int = 10_000) -> None:
    """
    连续尝试直到生成 n_struct 个有效结构 VASP 文件

    Parameters
    ----------
    n_struct : int
        目标结构数
    out_dir : str
        输出目录
    prefix : str
        文件名前缀
    group_range : (int, int)
        随机空间群范围（闭区间）
    factor : float
        分子间距因子
    random_seed : int or None
        为可重复结果设置随机种子
    max_trials : int
        最多尝试次数（防止死循环）
    """

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    generated = 0
    trials = 0
    serial = 0            # 文件序号，确保不覆盖
    while generated < n_struct and trials < max_trials:
        trials += 1
        group = random.choice(group_range)
        print(f"random_spg_group:{group}")
        xtal = pyxtal(molecular=True)
        try:
            xtal.from_random(
                dim=3,
                group=group,
                species=species,
                numIons=numIons,
                factor=factor,
            )
        except:
            pass

        if xtal.valid:
            stru = xtal.to_pymatgen()
            # 找到不冲突的文件名
            while True:
                fname = f"{prefix}_{group}_{serial}.vasp"
                fpath = out_path / fname
                if not fpath.exists():
                    stru.to(fmt="poscar", filename=str(fpath))
                    print(f"✓ 生成成功: {fpath.relative_to(out_path)}")
                    generated += 1
                    serial += 1
                    break
                serial += 1
        else:
            # 可根据需要打印调试信息
            pass

    if generated < n_struct:
        print(f"⚠️  提前结束: 仅生成 {generated}/{n_struct} 个结构 "
              f"(尝试次数 {trials}/{max_trials})")
    else:
        print(f"🎉 完成: 共生成 {generated} 个结构，保存在 {out_path.resolve()}")

# ---------- 3. 示例调用 ----------
if __name__ == "__main__":
    # ---------- 1. 定义分子 ----------
    la_mol = pyxtal_molecule(Molecule(["La"], [[0.0, 0.0, 0.0]]))
    diborane_mol = pyxtal_molecule("B2H6_D3d.xyz")   # 也可换成 B2H6_staggered.xyz
    
    species = [la_mol, diborane_mol]
    numIons = [2,2]            # 2a ×1  +  4d ×1
    spg_group = ([79, 80, 82, 87, 88, 97, 98] + list(range(107, 111)) + list(range(119, 123)) + list(range(139, 143)))
    
    # species = [la_mol, diborane_mol]
    # numIons = [2,2]            # 2a ×1  +  4d ×1
    # spg_group = list(range(1, 231))

    print(spg_group)
    # ---------- 2. 生成函数 ----------
    generate_structures(
        n_struct=20,          # 想要生成的结构数
        out_dir="structures", # 输出到子目录
        prefix="LaB2H6",      # 文件名前缀
        group_range = spg_group,
        factor=2.0,           # 分子间距
    )
