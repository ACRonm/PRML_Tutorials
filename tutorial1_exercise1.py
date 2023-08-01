import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
x = np.array([1,2,3,4,5])
y= np.array([2,4,6,8,10])

# Reshape the feature array
x = x.reshape(-1,1)

# Define the degree of the polynomial
degree = 3

# Create the polynomial features
polynomial_features = PolynomialFeatures(degree=degree)
x_poly = polynomial_features.fit_transform(x)

# Create and train the polynomial progression model 
model = LinearRegression()
model.fit(x_poly, y)

# Generate the data for plotting
x_plot = np.linspace(0, 6, 100).reshape(-1,1)
x_plot_poly = polynomial_features.fit_transform(x_plot)

y_plot = model.predict(x_plot_poly)

# Plot the data
plt.scatter(x, y, s=10)
plt.plot(x_plot, y_plot, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial fit of degree {}'.format(degree))
plt.show()