# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# metrics to evaluate the linear regression model
from sklearn.metrics import mean_squared_error, mean_absolute_error

# split the data into training and testing sets
from sklearn.model_selection import train_test_split

# import the linear regression model
from sklearn.linear_model import LinearRegression

# read the iris data
iris_dataset = pd.read_csv('./iris/iris.data', sep=',', names=[
    "sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

x = iris_dataset.drop(labels='species', axis=1)

x = x.drop(labels='petal_width', axis=1)

y = iris_dataset['petal_width']

# split into training and testing sets with ratio of 3:1
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=1)


lre = LinearRegression()

# train with linear regression
lre.fit(x_train, y_train)

# predict the test set
pred = lre.predict(x_test)

print("The Absolute Mean Error is:", mean_absolute_error(y_test, pred))
print("The Squared Mean Error is:", mean_squared_error(y_test, pred))
print("Mean Root Squared Error is:",
      np.sqrt(mean_squared_error(y_test, pred)))

abs(y_test - pred)

# visualise the results
plt.scatter(x_test[['sepal_length']], y_test,  color='red',
            label="Actual petal width")
plt.scatter(x_test[['sepal_length']], pred, color='green',
            label="Predicted petal width")
plt.legend()
plt.xlabel("Sepal Length in cm")
