#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
#Imprima as consoantes.

lista = 'psicose'
vogal = ['a','e','i','o','u']
for l in lista:
    if l not in vogal:
         print(l)