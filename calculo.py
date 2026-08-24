import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
T = 1000 / (50 - x)

cargas = [10, 20, 30, 40, 45, 48, 49, 49.5, 49.9]

limite_esquerda = sp.limit(T, x, 50, dir='-')
limite_direita = sp.limit(T, x, 50, dir='+')

print("Limite à esquerda de T(x) quando x se aproxima de 50:", limite_esquerda)
print("Limite à direita de T(x) quando x se aproxima de 50:", limite_direita)

for carga in cargas:
    tempo = 1000 / (50 - carga)
    print(f"{carga} req/s -> {tempo:.2f} ms")