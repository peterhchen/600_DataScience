# more than one dimension
import numpy as np
from random import randint
a = np.array([[1, 2], [3, 4]])

print ('a:')
print(a)
print ('a.shape:', a.shape)
# [[1, 2]
#  [3, 4]]

b = np.array([1, 2, 3, 4])

print ('\nb:')
print(b)
print ('b.shape:', b.shape)

c = np.array([[1, 2, 3, 4]])

print ('\nc:')
print(c)
print ('c.shape:', c.shape)

# data preprocessed
train_labels = []
train_samples = []

for i in range(5):
    random = randint(13,64)
    train_samples.append(random)
    train_labels.append(1)

train_labels = np.array(train_labels)
train_samples = np.array(train_samples)

x = np.array(train_samples)
y = np.array(train_labels)
print('\nx.shape:', x.shape)
print('x:', x)
print('\ny.shape:', y.shape)
print('y:', y)