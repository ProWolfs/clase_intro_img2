from utiles import img_letras
import matplotlib.pyplot as plt

lt = 'atatat'
img_list = img_letras(lt)

for img in img_list:
    plt.figure(figsize=(5,5))
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
plt.show()
