#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n2 = float(input("Nota 3: "))
n3 = float(input("Nota 4: "))
n4 = float(input("Nota 5: "))
media = 0
notas = [n1,n2,n3,n4]
for nota in notas:
    media += nota 
print(media / len(notas))