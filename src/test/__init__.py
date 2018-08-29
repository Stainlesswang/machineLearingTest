# -*- coding: utf-8 -*-
from pyspark.conf import SparkConf
import sys
from pyspark.context import SparkContext
if __name__ == "__main__":
    master = "local"
    if len(sys.argv) == 2:
        master = sys.argv[1]
    sc = SparkContext(master, "WordCount")
#     把程序已有的集合交给 parallelize()方法,就可以做操作
    lines = sc.parallelize(["sdddd", "i like pandas"])
    result = lines.flatMap(lambda x: x.split(" ")).countByValue()
    for  value in result:
        print ("%s " % (value))