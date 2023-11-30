import sys
import os

# sys.path.append('/Users/macbookpro/pyxtal_code/read_pyxtal-master/pyxtal')

from pyxtal import pyxtal
from pyxtal.molecule import pyxtal_molecule
from pymatgen.core.structure import Molecule
from numpy.random import randint, uniform, choice
from pyxtal.lattice import Lattice



unit1 = Molecule.from_file("F:\PyXtal\my_exercise\dodecahedron\\12.xyz")
unit2 = Molecule(species=['Sc'], coords=[[0.0, 0.0, 0.0]])

crystal_px = pyxtal(molecular=True)

seed_H4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for i in range(10000000):
    spg_num = randint(195, 230)
    units_num = choice(seed_H4, 1, replace=True)
    a = uniform(4.0, 6.0)

    lat = Lattice.from_para(a, a, a, 90, 90, 90)

    try:
        crystal_px.from_random(
            3,
            spg_num,
            [unit1, unit2],
            [1, 1],
            lattice=lat,
        )
    except:
        print("产生结构失败")
        continue

    print("-------------------产生结构成功----------------")
    ase_struc = crystal_px.to_ase()
    cry_name = "unit" + str(units_num) + ".vasp"
    p = "F:\PyXtal\my_exercise\dodecahedron\structures"
    path = os.path.join(p, cry_name)
    ase_struc.write(path, format='vasp', vasp5=True, direct=True)
