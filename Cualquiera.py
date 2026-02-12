import numpy as np
import matplotlib.pyplot as plt

a = np.array ([[255,0,255],[0,255,0],[0,0,0],[0,255,0]])
print(a)
print(a.shape)

plt.figure(figsize=(5,5))
plt.imshow(a, cmap='gray' , vmin=0, vmax=255)
plt.axis('off')
plt.show()