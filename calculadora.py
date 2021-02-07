operacao = input("digite a operacao desejada(soma,sub,mult,div): ")
numero1 = input("digite o primeiro numero: ")
numero2 = input("digite o segundo numero: ")

if operacao == "soma":
    resultado = int(numero1) + int(numero2)
elif operacao == "sub":
    resultado = int(numero1) - int(numero2)
elif operacao == "mult":
    resultado = int(numero1) * int(numero2)
elif operacao == "div":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "operacao nao suportada"

print("O resultado da operacao é: " + str(resultado))