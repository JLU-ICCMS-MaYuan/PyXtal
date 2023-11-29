import sys
import os

# sys.path.append('/Users/macbookpro/pyxtal_code/read_pyxtal-master/pyxtal')

from pyxtal import pyxtal
from pyxtal.molecule import pyxtal_molecule
from pymatgen.core.structure import Molecule
from numpy.random import randint, uniform, choice
from pyxtal.lattice import Lattice

xyz2 = """5
XH4
B     0.        0.        0.    
H     0.6276    0.6276    0.6276
H     0.6276   -0.6276   -0.6276
H    -0.6276    0.6276   -0.6276
H    -0.6276   -0.6276    0.6276
"""

mol2 = Molecule.from_str(xyz2, fmt='xyz')


BH4_unit = pyxtal_molecule(mol2)


crystal_La_B_Li_H = pyxtal(molecular=True)

seed_H4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for i in range(10000000):
    spg_num = randint(1, 230)
    BH4_num = choice(seed_H4, 1, replace=True)
    a = uniform(4.0, 6.0)

    l1 = Lattice.from_para(a, a, a, 90, 90, 90)
    try:
        crystal_La_B_Li_H.from_random(3, spgnum, [BH4_unit],
                                      [BH4_num], lattice=l1)
    except:
        print("产生结构失败")
        continue

    print("-------------------产生结构成功----------------")
    ase_struc = crystal_La_B_Li_H.to_ase()
    cry_name = "BH4_" + str(BH4_unit) + ".vasp"
    p = "/Users/macbookpro/pyxtal_code/read_pyxtal-master/create_cage_crystal/crystal_BH4"
    path = os.path.join(p, cry_name)
    ase_struc.write(path, format='vasp', vasp5=True, direct=True)
