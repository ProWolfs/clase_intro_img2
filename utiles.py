import numpy as np
import matplotlib.pyplot as plt

def img_letra(lt):
    if lt == 'a':
        return np.array ([[0,0,0],[0,255,0],[0,0,0],[0,255,0]])
    elif lt == 't':
        return np.array([[0,0,0],[255,0,255],[255,0,255],[255,0,255]])
    else:
        raise ValueError("Letra no reconocida.")
    
def img_letras(letras):
    letras_split = list(letras)
    imgs_list = [img_letra(lt) for lt in letras_split]
    return imgs_list
    