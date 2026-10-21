import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Bandeira de Taiwan")

img = np.zeros((15, 25, 3), dtype=np.uint8)

img[:, :] = (254, 0, 0)

img[0:8, 0:11] = (0, 0, 149)

img[2:6, 3:7] = (255, 255, 255)

img[1, 4:6] = (255, 255, 255)
img[6, 4:6] = (255, 255, 255)
img[3:5, 2] = (255, 255, 255)
img[3:5, 7] = (255, 255, 255)

img[2, 3] = (255, 255, 255)
img[2, 6] = (255, 255, 255)
img[5, 3] = (255, 255, 255)
img[5, 6] = (255, 255, 255)

st.image(ampliar(img))