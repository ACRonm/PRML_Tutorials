# Created on Sun Aug 17 9:53am 2023

# @author: u3204426

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('./iris/iris.data', sep=',', names=[
                   'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

print(iris["species"].value_counts())


print("=============================================================")

print(iris['species'])
