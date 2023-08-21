from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("jokowi.jpeg")
image_array = np.asanyarray(image)

print(image_array.shape)

plt.imshow(image_array)
plt.show()