import os
from pyxtal import pyxtal
from pyxtal.tolerance import Tol_matrix

from ase.io.xyz import write_xyz
from pyxtal.molecule import pyxtal_molecule

my_tm = Tol_matrix(
    ('H', 'H', 1.6)
)

mol_gen = pyxtal(molecular=False)
mol_gen.from_random(
    dim=0,
    group='Ih',
    species=['H'],
    numIons=[12],
    tm=my_tm
)
ase_struct = mol_gen.to_ase()
print(ase_struct)
name = '20.xyz'
dirspath = 'F:\PyXtal\my_exercise\icosahedron'
filepath = os.path.join(dirspath, name)
with open(filepath, 'w') as f:
    write_xyz(f, [ase_struct], comment='regular icosahedron')


