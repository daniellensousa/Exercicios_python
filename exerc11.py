#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite seu úsuario: ")
senha = input("Digite sua senha: ")

while senha == nome:
    print("A sua senha não pode ser igual ao nome do úsuario!")
    print("Digite novamente: ")
    nome = input("Digite seu úsuario: ")
    senha = input("Digite sua senha: ")
print("Bem vindo(a)!!!")



