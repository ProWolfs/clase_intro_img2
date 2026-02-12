import numpy as np
import matplotlib.pyplot as plt

a = 255-np.array ([[255,255,255],[255,0,255],[255,255,255],[255,0,255]])
print(a)
print(a.shape)
t = np.array([[0,0,0],[255,0,255],[255,0,255],[255,0,255]])

plt.figure(figsize=(5,5))
plt.imshow(a, cmap='gray' , vmin=0, vmax=255)
plt.axis('off')

plt.figure(figsize=(5,5))
plt.imshow(t, cmap='gray' , vmin=0, vmax=255)
plt.axis('off')

esp_peq = np.ones((1,3))*255
txt_h = np.concatenate([a,esp_peq,t],axis=0)

plt.figure(figsize=(10,5))
plt.imshow(txt_h, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()