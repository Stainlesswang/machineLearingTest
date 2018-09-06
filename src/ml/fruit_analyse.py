# coding=utf-8
"""
简单决绝水果分类问题
 使用数据分析工具,
 来读取 fruit_data_with_colors.txt中的59个不同种类的水果及各种特性
"""
# pandas是python的一个数据分析包
import pandas as pd
# matplotlib 是一个 Python 的 2D绘图库
import matplotlib.pyplot as plt
import seaborn as sns
import pylab as pl


# 使用数据分析工具读取txt文档数据
fruits = pd.read_table('fruit_data_with_colors.txt')

'''水果名称数量统计'''


def fruit_count():
    sns.countplot(fruits['fruit_name'], label="Count")
    plt.show()


'''箱型图'''


def show_box():
    fruits.drop('fruit_label', axis=1).plot(kind='box', subplots=True, layout=(2, 2),
                                            sharex=False, sharey=False, figsize=(9, 9),
                                            title='Box Plot for each input variable')
    plt.savefig('fruits_box')
    plt.show()


'''柱状图'''


def show_histogram():
    fruits.drop("fruit_label", axis=1).hist(bins=30, figsize=(9, 9))
    pl.suptitle("Histogram for each numeric input variable")
    plt.savefig('fruits_hist')
    plt.show()


# 执行方法
if __name__ == '__main__':

    # 数据的前五行
    # print(fruits.head(5))
    #  数据某些属性的值
    # print(fruits['fruit_name'].unique())
    # 数据的特征
    # print(fruits.shape)
    # show_box()
    # show_histogram()
    print('this is the demo how to change fruit')
