#Part 1: Deteccion de palindromos, tanto numeros como palabras
def EsPalindrome(i):
    i = str(i)
    #Convierte el numero en un string
    if i == i[::-1]:
        #Compara el string con su reverso
        print("True is a palindrome")
        #Si es igual, es un palindromo
    else:
        #Si no es igual, no es un palindromo
        print("False, no is a palindrome")


#Pruebas 1:
EsPalindrome(242)
#Pruebas 2:
EsPalindrome(45678654)
#Pruebas 3:
EsPalindrome(10102020101)
#Pruebas 4:
EsPalindrome("awa sts awa")
#Pruebas 5:
EsPalindrome("awta")


#Part 2: Deteccion de palindromos, que devuelvan numeros primos enteros mayores al valor dado

def PalindromePrimo(n):
    #Se define la funcion
    for i in range(n+1, 1000000):
        #Se establece el rango de numeros a evaluar
        if str(i) == str(i)[::-1] and all(i % o != 0 for o in range(2, i)):
            #Se evalua si el numero es primo y palindromo
            print(i)
            #Se imprime el numero
            break
            #Se detiene el loop

#Pruebas 1:
PalindromePrimo(13)
#Pruebas 2:
PalindromePrimo(8)
#Pruebas 3:
PalindromePrimo(6)

