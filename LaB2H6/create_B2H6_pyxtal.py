from pyxtal.symmetry import Group
from pyxtal import pyxtal
from pymatgen.core.structure import Molecule as PMGMolecule

diborane_cluster = pyxtal()
diborane_cluster.from_random(
    dim=0,
    group='D3d',     
    species=['B', 'H'],
    numIons=[2,6],
    factor=2.0,       
)

pmg_mol = PMGMolecule.from_sites(diborane_cluster.to_pymatgen().sites)
pmg_mol.to(fmt='xyz', filename='B2H6_D3d.xyz')