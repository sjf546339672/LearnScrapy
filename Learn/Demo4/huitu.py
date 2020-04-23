# coding: utf-8

import matplotlib
import matplotlib.pyplot as plt  # 数据可视化

matplotlib.rcParams["font.sans-serif"] = ["simhei"]  # 配置字体
matplotlib.rcParams["font.family"] = "sans-serif"

plt.bar([1], [123], label=u"广东")
plt.bar([2], [133], label=u"杭州")
plt.bar([3], [143], label=u"上海")
plt.bar([4], [153], label=u"北京")
plt.bar([5], [163], label=u"深圳")

plt.legend()
plt.show()
