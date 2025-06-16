import sys

from pymatgen.core.structure import Molecule
from pymatgen.symmetry.analyzer import PointGroupAnalyzer

# 构建一个分子（可从文件读入）
mol = Molecule.from_file(sys.argv[1])

# 识别点群
analyzer = PointGroupAnalyzer(mol)
print("点群是：", analyzer.get_pointgroup())      # 输出如 'D2h'
print("完整点群符号：", analyzer.sch_symbol)     # 输出如 'D2h-10'

# 可视化或获取操作
print("对称操作总数：", len(analyzer.symmops))