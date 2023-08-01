import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
x = np.array([[1200, 2, 1, 1995],
              [1800, 3, 2, 2002],
              [1800, 2, 2, 1985],
              [1350, 2, 1, 1998],
              [2000, 4, 3, 2010],])

y = np.array([250, 320, 280, 300, 450])

# Create and train the linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict the house prices
new_data = np.array([[1650, 3, 2, 2005],
                     [1400, 2, 1, 2000]])


prediction = model.predict(new_data)

print('Predicted house prices: ', prediction)
