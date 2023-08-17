# %%


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# read the iris data
iris_dataset = pd.read_csv('./iris/iris.data', sep=',', names=[
                           "sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

iplot = iris_dataset['species']\
    .value_counts()\
    .plot(kind="pie", autopct="%.2f", figsize=(8, 8), title="Iris Species")

iplot.set_ylabel('')


sc = iris_dataset[iris_dataset.species == "Iris-setosa"].plot(
    kind="scatter", x="sepal_length", y="sepal_width", color="red", label="Setosa")

iris_dataset[iris_dataset.species == "Iris-versicolor"].plot(
    kind="scatter", x="sepal_length", y="sepal_width", color="green", label="Versicolor", ax=sc)

iris_dataset[iris_dataset.species == "Iris-virginica"].plot(
    kind="scatter", x="sepal_length", y="sepal_width", color="orange", label="Virginica", ax=sc)

sc.set_xlabel("Sepal Length in cm")
sc.set_ylabel("Sepal Width in cm")
sc.set_title("Sepal Length vs Width")

iris_dataset.boxplot(by="species", figsize=(12, 6))

plt.show()

# %%
