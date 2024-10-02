def calculadora():
    while True:
        # Exibe o menu de operações
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        # Solicita a escolha do usuário
        opcao = input("\nDigite o número da operação: ")

        # Verifica se a opção é de saída
        if opcao == '0':
            print("Saindo do programa...")
            break

        # Verifica se a opção é válida
        elif opcao in ['1', '2', '3', '4']:
            try:
                # Solicita os números
                num1 = float(input("\nDigite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                # Realiza a operação com base na escolha
                if opcao == '1':
                    resultado = num1 + num2
                    print(f"\nO resultado da soma é: {resultado}")
                elif opcao == '2':
                    resultado = num1 - num2
                    print(f"\nO resultado da subtração é: {resultado}")
                elif opcao == '3':
                    resultado = num1 * num2
                    print(f"\nO resultado da multiplicação é: {resultado}")
                elif opcao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"\nO resultado da divisão é: {resultado}")
                    else:
                        print("\nErro: Divisão por zero não é permitida!")
            except ValueError:
                print("\nErro: Você deve digitar números válidos.")

        # Caso a opção seja inválida
        else:
            print("\nEssa opção não existe. Tente novamente.")

# Função principal para iniciar a calculadora
if __name__ == "__main__":
    calculadora()
