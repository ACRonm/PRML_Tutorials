# %%

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_openml
# %%

# Load the MNIST data
mnist = fetch_openml('mnist_784', version=1, cache=True)

X = mnist.data
y = mnist.target

X.shape
# %%

"""
Explanation of logistic regression with L1 and L2 regularisation:



"""


# Initialise the logistic regression model with L1 regularisation
logreg_l1 = LogisticRegression(penalty='l1', solver='saga', tol=0.1)

num_folds = 5

scores_l1 = cross_val_score(logreg_l1, X, y, cv=num_folds, scoring='accuracy')

average_accuracy_l1 = np.mean(scores_l1)

print('Average accuracy with L1 regularisation: {0:.4f}'.format(
    average_accuracy_l1))


# Initialise the logistic regression model with L2 regularisation
