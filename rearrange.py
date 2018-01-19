"""
Rearrange characters in a string such that no two adjacent are same

Given a string with repeated characters, task is rearrange characters in a string so that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.

Examples:

Input: aaabc
Output: abaca

Input: aaabb
Output: ababa

Input: aa
Output: Not Possible

Input: aaaabc
Output: Not Possible

"""

def cadenaALista(cadena):
    lista = []
    for i in cadena:
        lista.append(i)
    return lista

def rearrange(cadena):
    pila_letras = []
    pila_indices = []

    lista_cadena = cadenaALista(cadena)

    for i in range(0, len(cadena) - 1):
        if lista_cadena[i] == lista_cadena[i + 1] and (i+1) < len(cadena):
            pila_letras.append(lista_cadena[i])
            for j in range(i, len(cadena)):
                if lista_cadena[i + 1] != lista_cadena[j]:
                    temp = lista_cadena[j]
                    lista_cadena[j] = lista_cadena[i + 1]
                    lista_cadena[i + 1] = temp
                    pila_letras.pop()
                    break

    if len(pila_letras) == 0:
        return lista_cadena
    else:
        print('No es posible')
        return []


print(rearrange('aaabc'))

print(rearrange('aaabb'))

print(rearrange('aaaabc'))

print(rearrange('geeksforgeeks'))
