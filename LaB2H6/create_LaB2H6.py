# -*- coding: utf-8 -*-
"""
La (2a)  +  B2H6 (4d)  in I4/mmm (#139)
"""

from pymatgen.core.structure import Molecule
from pyxtal import pyxtal
from pyxtal.molecule import pyxtal_molecule
from pyxtal.lattice import Lattice
# ---------------- 1. 分子（刚体） ----------------
# (a) La 当成“单原子分子”
la_mol = pyxtal_molecule(Molecule(["La"], [[0.0, 0.0, 0.0]]))

# (b) 你的 B2H6（把文件名改成自己那份）
diborane_mol = pyxtal_molecule("B2H6_eclipsed.xyz")   # 也可换成 B2H6_staggered.xyz

# ---------------- 2. 构造分子晶 ----------------
xtal = pyxtal(molecular=True)  # 创建一个分子晶对象
xtal.from_random(
    dim=3, 
    group=79,      # 也可用 xtal.from_random(dim=3, group=139)
    species=[la_mol, diborane_mol],
    numIons=[2, 2],      # 2a×1 + 4d×1
    factor=2.0,          # 分子间距
    random_state=42,
    # lattice=Lattice(ltype=)  # 初始晶格参数
)

if xtal.valid:
    stru = xtal.to_pymatgen()
    stru.to(fmt="poscar", filename="LaB2H6_I4.vasp")
    print("✓ 写出 LaB2H6_I4.vasp")
else:
    print("⚠️  请把 factor 调大或更换 random_state 再试")
