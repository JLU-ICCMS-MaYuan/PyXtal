import numpy as np
from pymatgen.core.structure import Molecule

def write_b2h6(name, species, coords):
    mol = Molecule(species, coords)
    print(mol)
    mol.to(f"{name}.xyz", "xyz")
    print(f"✓ 写出：{name}.xyz")

# ========= D3d 构型（图 3） =========
# 两个硼沿 z 轴放置
d_BB = 1.75  # B–B 键长 (Å)；可根据文献或优化再调
d_BH = 1.19   # B–H 键长 (Å)
coords = [[0, 0, -d_BB/2],   # B1
          [0, 0,  d_BB/2]]   # B2
species = ["B", "B"]

# 3 个 H 环绕 B1，角度 0/120/240°
for k in range(3):
    phi = k * 2*np.pi/3
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi), -d_BB/2])
    species.append("H")
offset = np.pi/3
for k in range(3):
    phi = k * 2*np.pi/3 + offset
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi),  d_BB/2])
    species.append("H")
write_b2h6("B2H6_D3d", species, coords)

# ========= D3h 构型（图 4） =========
# 两 B 和终端氢在 XY 平面，桥氢上下对称
# 两个硼沿 z 轴放置
d_BB = 1.75  # B–B 键长 (Å)；可根据文献或优化再调
d_BH = 1.19   # B–H 键长 (Å)
coords = [[0, 0, -d_BB/2],   # B1
          [0, 0,  d_BB/2]]   # B2
species = ["B", "B"]

# 3 个 H 环绕 B1，角度 0/120/240°
for k in range(3):
    phi = k * 2*np.pi/3
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi), -d_BB/2])
    species.append("H")
for k in range(3):
    phi = k * 2*np.pi/3
    coords.append([d_BH*np.cos(phi), d_BH*np.sin(phi),  d_BB/2])
    species.append("H")
write_b2h6("B2H6_D3h", species, coords)

# ========== D2d 构型 ==========
coords = [
[ -0.885000,  0.000000,  0.000000],
[  0.885000,  0.000000,  0.000000],
[  0.000000,  0.000000,  0.992800],
[  0.000000,  0.000000, -0.992800],
[ -1.462000,  1.040000,  0.000000],
[ -1.462000, -1.040000,  0.000000],
[  1.462000,  0.000000,  1.040000],
[  1.462000,  0.000000, -1.040000],
]
write_b2h6("B2H6_D2d", species, coords)

# ========== D2h 平面构型 ==========
species = ["B", "B",         # 两个 B
           "H", "H", "H",    # B1 端 H1, H2, 外延 H3
           "H", "H", "H"]    # B2 端 H4, H5, 外延 H6

coords = [
[-0.88500,   0.00000,   0.00000,],
[ 0.88500,   0.00000,   0.00000,],
[ 0.00000,   0.99280,   0.00000,],
[ 0.00000,  -0.99280,   0.00000,],
[-1.46200,   1.04000,   0.00000,],
[-1.46200,  -1.04000,   0.00000,],
[ 1.46200,   1.04000,   0.00000,],
[ 1.46200,  -1.04000,   0.00000,],
]
write_b2h6("B2H6_D2h_flat", species, coords)

# ========== D2h 立体构型 ==========
species = ["B", "B",         # 两个 B
           "H", "H", "H",    # B1 端 H1, H2, 外延 H3
           "H", "H", "H"]    # B2 端 H4, H5, 外延 H6
coords = [
[ -0.88500,   0.00000,   0.00000,],
[  0.88500,   0.00000,   0.00000,],
[  0.00000,   0.00000,   0.99280 ,],
[  0.00000,   0.00000,  -0.99280 ,],
[ -1.46200,   1.04000,   0.00000 ,],
[ -1.46200,  -1.04000,   0.00000 ,],
[  1.46200,   1.04000,   0.00000 ,],
[  1.46200,  -1.04000,   0.00000,],
]
write_b2h6("B2H6_D2h_3D", species, coords)
