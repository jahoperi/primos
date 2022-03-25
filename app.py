# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:00:34 2022

@author: jahop_fz60h0
"""



import json
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import base64
from streamlit_player import st_player


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_qb4hnhvz.json")




st_lottie(lottie_hello, key = "hello")



st.title("Distancia entre números primos")



st.subheader("Consideremos el conjunto W = {2n con n >= 4 en N | 2(4) = 8, 2(5) = 10, 2(6) = 12, 2(7) = 14, 2(8) = 16, 2(9) = 18, 2(10) = 20, 2(11) = 22, 2(12) = 24, 2(13) = 26, 2(14) = 28, 2(15) = 30, 2(16) = 32, 2(17) = 34, 2(18) = 36, 2(19) = 38, 2(20) = 40, 2(21) = 42, 2(22) = 44, 2(23) = 46, 2(24) = 48, 2(25) = 50, 2(26) = 52, 2(27) = 54,...}")
st.subheader('') 
st.subheader('Distancia-2') 
st.subheader('') 
st.subheader('Consideremos el intervalo [n -1 , n -1]')
st.subheader('')

st.subheader('Para:')
st.subheader('n = 4, [4 -1, 4 + 1], 3 + 5 = 8   -------- caso(i)')
st.subheader('n = 5, [5 - 1, 5 + 1], 4 + 6 = 10 ------ caso(iv)')
st.subheader('n = 6, [6 -1, 6 + 1], 5 + 7 = 12  ------ caso(i)')
st.subheader('n = 7, [7 -1, 7 + 1], 6 + 8 = 14  ----- caso(iv)')
st.subheader('n = 8, [8 - 1, 8 + 1], 7 + 9 = 16 ----- caso(ii)')
st.subheader('n = 9, [9 - 1, 9 + 1], 8 + 10 = 18 ----- caso (iv)')
st.subheader('n = 10, [10 -1, 10 + 1], 9 + 11 = 20 ----- caso(iii)')
st.subheader('n = 11, [11 -1, 11 + 1], 10 + 12 = 22 ----- caso(iv)')

st.subheader('n = 12, [12 -1, 12 + 1], 11 + 13 = 24   -------- caso(i)')
st.subheader('n = 13, [13 - 1, 13 + 1], 12 + 14 = 26 ------ caso(iv)')
st.subheader('n = 14, [14 -1, 14 + 1], 13 + 15 = 28  ------ caso(ii)')
st.subheader('n = 15, [15 -1, 15 + 1], 14 + 16 = 30  ----- caso(iv)')
st.subheader('n = 16, [16 - 1, 16 + 1], 15 + 17 = 32 ----- caso(iii)')
st.subheader('n = 17, [17 - 1, 17 + 1], 16 + 18 = 34 ----- caso (iv)')
st.subheader('n = 18, [18 -1, 18 +1], 17 + 19 = 36 ----- caso(i)')
st.subheader('n = 19, [19 -1, 19 + 1], 18 + 20 = 38 ----- caso(iv)')

st.subheader('n = 20, [20 -1, 20 + 1], 19 + 21 = 40   -------- caso(ii)')
st.subheader('n = 21, [21 - 1, 21 + 1], 20 + 22 = 42 ------ caso(iv)')
st.subheader('n = 22, [22 -1, 22 + 1], 21 + 23 = 44  ------ caso(iii)')
st.subheader('n = 23, [23 -1, 23 + 1], 22 + 24 = 46  ----- caso(iv)')
st.subheader('n = 24, [24 - 1, 24 + 1], 23 + 25 = 48 ----- caso(ii)')
st.subheader('n = 25, [25 - 1, 25 + 1], 24 + 26 = 50 ----- caso (iv)')
st.subheader('n = 26, [26 -1, 26 +1], 25 + 27 = 52 ----- caso(v)')
st.subheader('n = 27, [27 -1, 27 +1], 26 + 28 = 54 ----- caso(iv)')

st.subheader('Se presentan cinco casos:')
st.subheader('i) [p, p + 2], p es número primo')
st.subheader('ii) [p, t], t número impar no primo')
st.subheader('iii) [t , p]')
st.subheader('iv) [s , s + 2], s es número par')
st.subheader('v)) [t , t + 2]')


st.subheader('')
st.subheader('Sean los siguientes conjuntos:')
st.subheader('')
st.subheader('A1 = {[p, p + 2] que pertenecen al conjunto W | es el caso (i)}')
st.subheader('A2 = {[p, t] que pertenecen al conjunto W | es el caso (ii)}')
st.subheader('A3 = {[t, p] que pertenecen al conjunto W | es el caso (iii)}')
st.subheader('A4 = {[s, s + 2] que pertenecen al conjunto W | es el caso (iv)}')
st.subheader('A5 = {[t, t + 2] que pertenecen al conjunto W | es el caso (v)}')
st.subheader('')
st.subheader('Observemos que:')
st.subheader('')
st.subheader('A1 = {8, 12, 24, 36}')
st.subheader('')
st.subheader('A2 = {16, 28, 40, 48}')
st.subheader('')
st.subheader('A3 = {20, 32, 44}')
st.subheader('')
st.subheader('A4 = {10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54}')
st.subheader('')
st.subheader('A5 = {52}')
st.subheader('')
st.subheader('Luego,')
st.subheader('')
st.subheader('(A1 U A2 U A3 U A4 U A5) = {8, 10, 12,14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54} nota: truncado en n = 27')
st.subheader('')
st.subheader('Es decir.')
st.subheader('')
st.subheader('W = (A1 U A2 U A3 U A4 U A5), (nota: truncado en n = 27)')
st.subheader('')
st.subheader('si W ⊂ (A1 U A2 U A3 U A4 U A5)')
st.subheader('y')
st.subheader('')
st.subheader('(A1 U A2 U A3 U A4 U A5) ⊂ W')
st.subheader('')
st.subheader('lo que implica')
st.subheader('A1 ⊂ W')
st.subheader('')
st.subheader('A2 ⊂ W')
st.subheader('')
st.subheader('A3 ⊂ W')
st.subheader('')
st.subheader('A4 ⊂ W')
st.subheader('')
st.subheader('A5 ⊂ W')
st.subheader('Tomemos ahora en ambos lados la cardinalidad de los conjuntos')
st.subheader('')
st.subheader('|W| = |(A1 U A2 U A3 U A4 U A5)|, para que la igualdad entre conjuntos se conserve (nota: truncado en n = 27)')
st.subheader('')
st.subheader('Pero, sabemos que')
st.subheader('|W| = ∞, (nota: si n = 4, 5, 6, 7, 8,...)')
st.subheader('')
st.subheader('y')
st.subheader('')
st.subheader('|A1 U A2 U A3 U A4 U A5| = ∞, para que la igualdad entre los conjuntos se conserve (nota: siempre que n = 4, 5, 6, 7, 8,...)')
st.subheader('')
st.subheader('Observación: |(A1 U A2 U A3 U A4 U A5) | = ∞, si al menos uno de los conjuntos A1 ó A2 ó A3 ó A4 ó A5 tiene cardinalidad infinita')
st.subheader('')
st.subheader('Por simplicidad, consideramos que |A4| = ∞, |A1| = finita,  |A2| = finita, |A3| = finita y |A5| = finita')
st.subheader('')
st.subheader('He tomado el conjunto A4, porque el patrón es que los números que pertenecen a este conjunto, empieza en 10 y van sumando en 4 unidades')
st.subheader('')
st.subheader('Entonces el conjunto (A1 U A2 U A3 U A4 U A5) nos quedaría')
st.subheader('')
st.subheader('(A1 U A2 U A3 U A4 U A5) = {8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, ...}')
st.subheader('')
st.subheader('Notese que el último número es el 54 que está en el conjunto A4 y que suponemos tiene cardinalidad infinita; entonces vamos sumando de 4 unidades')
st.subheader('')
st.subheader('54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102,...')
st.subheader('')
st.subheader('¿Como tapamos los huecos comprendidos en?')
st.subheader('')
st.subheader('54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102,...')
st.subheader('')
st.subheader('Faltan los números:')
st.subheader('')
st.subheader('56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100,...')
st.subheader('')
st.subheader('faltan en el conjunto A1 los números: 60, 84')
st.subheader('')
st.subheader('A1 = {8, 12, 24, 36, 60 = 29 + 31, 84 = 41 + 43} Nota: para tapar hasta 102 nada más')
st.subheader('')
st.subheader('faltan en el conjunto A2 los números: 64, 76, 88, 96')
st.subheader('')
st.subheader('A2 = {16, 28, 40, 48, 64 = 31 + 33, 76 = 37 + 39, 88 = 43 + 45, 96 = 47 + 49} Nota: para tapar hasta 102 nada más')
st.subheader('')
st.subheader('faltan en el conjunto A3 los números: 56, 72, 80, 92')
st.subheader('')
st.subheader('A3 = {20, 32, 44, 56 = 27 + 29, 72 = 35 + 37, 80 = 39 + 41, 92 = 45 + 47} Nota: para tapar hasta 102 nada más')
st.subheader('faltan en el conjunto A5 los números: 68, 100')
st.subheader('')
st.subheader('A5 = {52, 68 = 33 + 35, 100 = 49 + 51} Nota: para tapar hasta 102 nada más')
st.subheader('')
st.subheader('Con este ejercicio, nos quedaría')
st.subheader('')
st.subheader('(A1 U A2 U A3 U A4 U A5) = {8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102,...} Nota: para tapar hasta 102 nada más')
st.subheader('')
st.subheader('Entonces, ya podemos concluir')
st.subheader('')
st.subheader('|W| = ∞ = |(A1 U A2 U A3 U A4 U A5)|, si |A1| = ∞ ( A1 ⊂ W) , |A2| = ∞ (A2 ⊂ W), |A3| = ∞ (A3 ⊂ W), |A4| = ∞ (A ⊂ W) y |A5| = ∞ (A5 ⊂ W) ')
st.subheader('')
st.subheader('Como')
st.subheader('')
st.subheader('|A1| = ∞')
st.subheader('')
st.subheader('impica que tenemos infinitas parejas de números primos de distancia-2')

st.subheader('')
st.subheader('')
st.subheader('')
st.subheader('')
def show_pdf(file_path):
    with open(file_path,"rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("papaer-1.pdf")

st.subheader('')
st.subheader('')

#st_player("https://www.youtube.com/watch?v=Lk7I5Qqo95U")
st_player("https://www.dailymotion.com/embed/video/x89crz9?autoplay=1")
st.subheader('')
st.subheader('')
st.header('JAVIER HORACIO PEREZ RICARDEZ') 
st.subheader('')  
st.subheader('Maestría en Ciencias de la Computación') 
st.subheader('')  
st.subheader('Cédula: 5290889') 
st.subheader('') 
st.subheader('Licenciatura en Matemáticas')  
st.subheader('') 
st.subheader('Cédula: 4431246') 
st.subheader('')  
st.subheader('Móvil: 993 291 3812') 
st.subheader('')  
st.subheader('email: jahoperi@gmail.com') 
