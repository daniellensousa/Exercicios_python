#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


#DIGITAR O NOME MAIOR QUE TRÊS CARACTERES, WHILE "ENQUANTO" NÃO FOR MAIOR QUE 3 CARACTERES, O "LOOP" CONTINUA!
nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Digite um nome maior que três caractere")
    print("Digite Novamente: ")
    nome = input("Digite seu nome: ")

#DIGITAR A IDADE MAIOR QUE 0 E MENOR QUE 150 NUMEROS, WHILE "ENQUANTO" NÃO FOR MAIOR QUE 0 OU MENOR QUE 150 O "LOOP" CONTINUA!
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Digite uma idade valida!")
    print("Digite Novamente: ")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salario: "))
while salario < 0:
    print("Digite um salario valido!")
    print("Digite Novamente: ")
    salario = float(input("Digite seu salario: "))

sexo = input('Digite seu sexo: ').lower()
while sexo != 'f' and sexo != 'm':
    print('erro somente aceitamos M ou F')
    sexo = input('Digite seu sexo: ').lower()

estado_civil = input("(s) solteiro(a) (c) casado, (v) viuvo, (d) divorciado: ")
lista = ['s','c', 'v', 'd']
while estado_civil not in lista:
    print('Digite as siglas: ')
    estado_civil = input("(s) solteiro(a) (c) casado, (v) viuvo, (d) divorciado: ")

print("Dados salvos!")



