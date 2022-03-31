#calculadora python
print("*"*20 + "CALCULADORA PYTHON" + "*"*20)
while True:
    print("SELECIONE O NÚMERO DA OPERAÇÃO DESEJADA:")
    print("1- SOMA \n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO")

    operador = input("DIGITE O NÚMERO DA SUA OPERAÇÃO: ")

    n1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    n2 = int(input("DIGITE O SEGUNDO NÚMERO: "))

    if operador == "1":
        resultado = n1 + n2
        print(f"{n1} + {n2} = {resultado}")
    elif operador == "2":
        resultado = n1 - n2
        print(f"{n1} - {n2} = {resultado}")
    elif operador == "3":
        resultado = n1 * n2
        print(f"{n1} * {n2} = {resultado}")
    elif operador == "4":
        resultado = n1 / n2
        print(f"{n1} / {n2} = {resultado}")
    else:
        print("ENTRADA INVÁLIDA")

    repetir = input("DESEJA FAZER OUTRA OPERAÇÃO? (s/n): ")
    if repetir == "n":
        break

