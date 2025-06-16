import numpy as np
from pymatgen.core.structure import Molecule

# === 参数 ===
d_BB = 2.0  # B–B 键长 (Å)；可根据文献或优化再调
d_BH = 1.19   # B–H 键长 (Å)
# mode  = "staggered"     # "staggered" → D3d,  "eclipsed" → D3h
mode = "eclipsed"  # 选择构型：交错 (staggered) 或重叠 (eclipsed)

# === 计算 ===
# 两个硼沿 z 轴放置
coords = [[0, 0, -d_BB/2],   # B1
          [0, 0,  d_BB/2]]   # B2
species = ["B", "B"]

# 3 个 H 环绕 B1，角度 0/120/240°
for k in range(3):
    phi = k * 2*np.pi/3
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi), -d_BB/2])
    species.append("H")

# 3 个 H 环绕 B2，若交错则整体多转 60°
offset = np.pi/3 if mode == "staggered" else 0.0
for k in range(3):
    phi = k * 2*np.pi/3 + offset
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi),  d_BB/2])
    species.append("H")

# === 构造分子 ===
diborane = Molecule(species, coords)
diborane.to(fmt="xyz", filename=f"B2H6_{mode}.xyz")
print(diborane)
