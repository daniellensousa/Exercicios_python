#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = (input("Qual o seu sexo? Digite (F) para feminino, (M) masculino, (N) não identificar: "))

if(sexo == "F"):
    print("Feminino")
elif(sexo == "M"):
    print("Masculino")
elif(sexo == "N"): 
    print("Não binario")



