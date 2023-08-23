# %%
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
# get mnist data
from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

labels = pd.Series(y_train).value_counts()

print(labels)

# %%
# normalise the data
X_train = X_train / 255.0
X_test = X_test / 255.0

# %%
# build the model

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128,
                          activation=tf.nn.relu),
    tf.keras.layers.Dense(10,
                          activation=tf.nn.softmax)
])

# %%
# compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# %%
# train the model

model.fit(X_train, y_train, epochs=10)

# %%
# evaluate the model

model.evaluate(X_test, y_test)

# %%
# make predictions

predictions = model.predict(X_test)

# %%
# plot the first 5 predictions

for i in range(5):
    plt.imshow(X_test[i], cmap=plt.cm.binary)
    plt.show()
    print("Prediction: ", predictions[i].argmax())
    print("Actual: ", y_test[i])

# %%
