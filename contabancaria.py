menu = """
DIGITE QUAL OPERAÇÃO DESEJA REALIZAR

[1] saldo em conta
[2] depositar
[3] sacar
[4] extrato
[0] sair

"""
saldo = 0
limite_saque = 500
numero_saques = 0
QUANTIDADE_SAQUE = 3
transacoes = [] 

while True:
    opcao = input(menu)

    if opcao == "1":
        print(f"Saldo em conta: R${saldo:.2f}")

    elif opcao == "2":
        valor_deposito = int(input("Valor do depósito:"))
        saldo += valor_deposito
        transacoes.append(("Depósito", valor_deposito))  

    elif opcao == "3":
        if numero_saques >= QUANTIDADE_SAQUE:
            print("Quantidade limite de saques atingido")
            break
        valor_saque = int(input("Valor do saque:"))
        if valor_saque > 500:
            print("O valor de cada saque deve ser no máximo R$500")
            break
        elif valor_saque > saldo:
            print("Saldo indisponível")
        else:
            saldo -= valor_saque
            numero_saques += 1
            transacoes.append(("Saque", valor_saque)) 

    elif opcao == "4":
        print("Extrato:")
        for tipo, valor in transacoes:
            print(f"{tipo}: R${valor}")
        print(f"Saldo final: R${saldo:.2f}")  

    elif opcao == "0":
        break

    else:
        print("Opção Inválida")