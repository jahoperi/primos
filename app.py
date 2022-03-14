# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:12:54 2022

@author: jahop_fz60h0
"""
import json
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_qb4hnhvz.json")




st_lottie(lottie_hello, key = "hello")



st.title("Distancia entre números primos")

st.subheader("Consideremos el conjunto 2W = {2n con n >= 2 en N | 2(2) = 4, 2(3) = 6, 2(4) = 8, 2(5) = 10, 2(6) = 12, 2(7) = 14, 2(8) = 16, 2(9) = 18...}")
st.subheader('') 
st.subheader('Distancia-0') 
st.subheader('') 
st.subheader('Consideremos el intervalo [n , n]')
st.subheader('')
st.subheader('Sólo se presentan tres casos:')
st.subheader('i) [p, p], p es número primo')
st.subheader('ii) [s, s], s es par')
st.subheader('iii) [t , t], t es número impar no primo')
st.subheader('Para:')
st.subheader('n = 2, [2, 2], 2 + 2 = 4 ------ caso(i)')
st.subheader('n = 3, [3, 3], 3 + 3 = 6 ------ caso(i)')
st.subheader('n = 4, [4, 4], 4 + 4 = 8 ------ caso(ii)')
st.subheader('n = 5, [5, 5], 5 + 5 = 10 ----- caso(i')
st.subheader('n = 6, [6, 6], 6 + 6 = 12 ----- caso(ii)')
st.subheader('n = 7, [7, 7], 7 + 7 = 14 ----- caso (i)')
st.subheader('n = 8, [8, 8], 8 + 8 = 16 ----- caso(ii)')
st.subheader('n = 9, [9, 9], 9 + 9 = 18 ----- caso(iii)')
st.subheader('')
st.subheader('Sean los siguientes conjuntos:')
st.subheader('')
st.subheader('A = {[p, p] que pertenecen al conjunto 2W | es el caso (i)')
st.subheader('Y = {[s, s] que pertenecen al conjunto 2W | es el caso (ii)')
st.subheader('Z = {[t, t] que pertenecen al conjunto 2W | es el caso (iii)')
st.subheader('')
st.subheader('Observemos que:')
st.subheader('')
st.subheader('2W = A ∪ Y ∪ Z')
st.subheader('')
st.subheader('Además,')
st.subheader('')
st.subheader('|2W| = ∞')
st.subheader('⇒ |A| = ∞ ')
st.subheader('⇒ |Y| = ∞ ')
st.subheader('⇒ |Z| = ∞ ')
st.subheader('')
st.subheader('Por lo tanto el conjunto A de numero primos de distancia-0, tiene cardinalidad infinita')
st.subheader('')
st.subheader('')
st.subheader('')


st.subheader("Consideremos el conjunto 2W = {2n con n >= 4 en N | 2(4) = 8, 2(5) = 10, 2(6) = 12, 2(7) = 14, 2(8) = 16, 2(9) = 18, 2(10) = 20, 2(11) = 22, 2(12) = 24, 2(13) = 26, 2(14) = 28, 2(15) = 30, 2(16) = 32, 2(17) = 34, 2(18) = 36, 2(19) = 38, 2(20) = 40, 2(21) = 42, 2(22) = 44, 2(23) = 46, 2(24) = 48, 2(25) = 50, 2(26) = 52, ...}")
st.subheader('') 
st.subheader('Distancia-2') 
st.subheader('') 
st.subheader('Consideremos el intervalo [n -1 , n -1]')
st.subheader('')
st.subheader('Se presentan cinco casos:')
st.subheader('i) [p, p + 2], p es número primo')
st.subheader('ii) [p, r], r número impar no primo')
st.subheader('iii) [r , p], r número impar no primo')
st.subheader('iv) [s , s + 2], s es número par')
st.subheader('v)) [t , t + 2], t es número impar no primo')

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


st.subheader('')
st.subheader('Sean los siguientes conjuntos:')
st.subheader('')
st.subheader('B = {[p, p + 2] que pertenecen al conjunto 2W | es el caso (i)}')
st.subheader('W = {[p, r] que pertenecen al conjunto 2W | es el caso (ii)}')
st.subheader('X = {[r, p] que pertenecen al conjunto 2W | es el caso (iii)}')
st.subheader('Y = {[s, s + 2] que pertenecen al conjunto 2W | es el caso (iv)}')
st.subheader('Z = {[t, t + 2] que pertenecen al conjunto 2W | es el caso (v)}')
st.subheader('')
st.subheader('Observemos que:')
st.subheader('')
st.subheader('2W = B ∪ W ∪ X ∪ Y ∪ Z')
st.subheader('')
st.subheader('Además,')
st.subheader('')
st.subheader('|2W| = ∞')
st.subheader('⇒ |B| = ∞ ')
st.subheader('⇒ |W| = ∞ ')
st.subheader('⇒ |X| = ∞ ')
st.subheader('⇒ |Y| = ∞ ')
st.subheader('⇒ |Z| = ∞ ')
st.subheader('')
st.subheader('Por lo tanto el conjunto B de numero primos de distancia-2 (primos gemelos), tiene cardinalidad infinita')
st.subheader('')
st.subheader('')
st.subheader('')



st.subheader("Consideremos el conjunto 2W = {2n con n >= 4 en N | 2(4) = 8, 2(5) = 10, 2(6) = 12, 2(7) = 14, 2(8) = 16, 2(9) = 18, 2(10) = 20, 2(11) = 22, 2(12) = 24, 2(13) = 26, 2(14) = 28, 2(15) = 30, 2(16) = 32, 2(17) = 34, 2(18) = 36, 2(19) = 38, 2(20) = 40, 2(21) = 42, 2(22) = 44, 2(23) = 46, 2(24) = 48, 2(25) = 50, 2(26) = 52, ...}")
st.subheader('') 
st.subheader('Distancia-4') 
st.subheader('') 
st.subheader('Consideremos el intervalo [n -2 , n -2]')
st.subheader('')
st.subheader('Se presentan cinco casos:')
st.subheader('i) [p, p + 4], p es número primo')
st.subheader('ii) [p, r], r número impar no primo')
st.subheader('iii) [r , p], r número impar no primo')
st.subheader('iv) [s , s + 4], s es número par')
st.subheader('v)) [t , t + 4], t es número impar no primo')

st.subheader('Para:')
st.subheader('n = 4, [4 -2, 4 + 2], 2 + 6 = 8   -------- caso(iv)')
st.subheader('n = 5, [5 - 2, 5 + 2], 3 + 7 = 10 ------ caso(i)')
st.subheader('n = 6, [6 -2, 6 + 2], 4 + 8 = 12  ------ caso(iv)')
st.subheader('n = 7, [7 -2, 7 + 2], 5 + 9 = 14  ----- caso(ii)')
st.subheader('n = 8, [8 - 2, 8 + 2], 6 + 10 = 16 ----- caso(iv)')
st.subheader('n = 9, [9 - 2, 9 + 2], 7 + 11 = 18 ----- caso (i)')
st.subheader('n = 10, [10 -2, 10 + 2], 8 + 12 = 20 ----- caso(iv)')
st.subheader('n = 11, [11 -2, 11 + 2], 9 + 13 = 22 ----- caso(iii)')
st.subheader('n = 12, [12 -2, 12 + 2], 10 + 14 = 24   -------- caso(iv)')
st.subheader('n = 13, [13 -2, 13 + 2], 11 + 15 = 24   -------- caso(ii)')


st.subheader('')
st.subheader('Sean los siguientes conjuntos:')
st.subheader('')
st.subheader('C = {[p, p + 4] que pertenecen al conjunto 2W | es el caso (i)}')
st.subheader('W = {[p, r] que pertenecen al conjunto 2W | es el caso (ii)}')
st.subheader('X = {[r, p] que pertenecen al conjunto 2W | es el caso (iii)}')
st.subheader('Y = {[s, s + 4] que pertenecen al conjunto 2W | es el caso (iv)}')
st.subheader('Z = {[t, t + 4] que pertenecen al conjunto 2W | es el caso (v)}')
st.subheader('')
st.subheader('Observemos que:')
st.subheader('')
st.subheader('2W = C ∪ W ∪ X ∪ Y ∪ Z')
st.subheader('')
st.subheader('Además,')
st.subheader('')
st.subheader('|2W| = ∞')
st.subheader('⇒ |C| = ∞ ')
st.subheader('⇒ |W| = ∞ ')
st.subheader('⇒ |X| = ∞ ')
st.subheader('⇒ |Y| = ∞ ')
st.subheader('⇒ |Z| = ∞ ')
st.subheader('')
st.subheader('Por lo tanto el conjunto C de numero primos de distancia-4, tiene cardinalidad infinita')
st.subheader('')
st.subheader('')
st.subheader('')

st.subheader('')
st.subheader('')
st.subheader('')


st.subheader('De manera análoga, se puede seguir para distancias entre números primos: 6, 8, 10, 12, 14, 16, ....')

st.subheader('')
st.subheader('Observese que tenemos los conjuntos A de distancia-0, B de dsitancia-2 y C de distancia-4 de números primos')
st.subheader('Entonces, todos los números pares mayores o iguales que 4, pueden ser representados como la suma de numeros primos')



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