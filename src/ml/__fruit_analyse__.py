'''
简单决绝水果分类问题
 使用数据分析工具,
 来读取 fruit_data_with_colors.txt中的59个不同种类的水果及各种特性
'''
#pandas是python的一个数据分析包
import pandas as pd
#matplotlib 是一个 Python 的 2D绘图库
import matplotlib.pyplot as plt
import seaborn as sns

fruits=pd.read_table('fruit_data_with_colors.txt')
print("展示数据的前五行:")
print(fruits.head(5))
print("看看水果名称有哪些?:")
print(fruits['fruit_name'].unique())
print("看看数据的特征:在数据集中有59个水果和7个特征:")
print(fruits.shape)
#数据可视化工具显示
sns.countplot(fruits['fruit_name'],label="Count")
plt.show()