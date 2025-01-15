import tensorflow as tf

# Define a simple computation
a = tf.constant(5.0)
b = tf.constant(6.0)
result = a * b
print("Result of multiplication:", result.numpy())
