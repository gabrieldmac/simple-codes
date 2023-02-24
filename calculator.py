# Receive data from console
def main():
    print("Entrou na main")
    primeiroValor = int(input("Digite o primeiro valor: "))
    segundoValor = int(input("Digite o segundo valor: "))
    operacao = input("Digite a operacao +,-,* ou /: ")

    resultado = 0
    if operacao == "+":
        resultado = primeiroValor + segundoValor
    elif operacao == "-":
        resultado = primeiroValor - segundoValor
    elif operacao == "/":
        resultado = primeiroValor / segundoValor
    elif operacao == "*":
        resultado = primeiroValor * segundoValor

    print(resultado)


if __name__ == "__main__":
    main()