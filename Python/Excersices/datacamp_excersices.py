import numpy as np

x = np.array([9, 5])
y = np.array([16, 12])

print(np.logical_or(x < 5, y > 15))

datacamp = { 'course':'python', 'level':'intermediate', 'lesson': {'dictionaries':'python', 'lists':'r' } }

datacamp.keys()

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

es_palindromo("Tenet")

