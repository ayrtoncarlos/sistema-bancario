from datetime import datetime
from pprint import pprint


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extratos = []
numero_saques = 0
LIMITE_SAQUES = 3

print(" SISTEMA BANCÁRIO ".center(30, '#'))

while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        print("Depósito")

        valor = float(input("Insira o valor para depósito: R$ "))

        if valor > 0:
            deposito = {
                "operação": "Depósito",
                "valor": f'R$ {valor:.2f}',
                "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "saldo_antes": f'R$ {saldo:.2f}',
                "saldo_depois": f'R$ {(saldo + valor):.2f}'
            }
            saldo += valor
            extratos.append(deposito)
            print("Depósito feito com sucesso!")
            print(f'Novo saldo: {saldo:.2f}')

    elif opcao == 's':
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Insira o valor para saque: R$ "))

            if valor <= LIMITE:
                if (saldo - valor) >= 0:
                    saque = {
                        "operação": "Saque",
                        "valor": f'R$ {valor:.2f}',
                        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        "saldo_antes": f'R$ {saldo:.2f}',
                        "saldo_depois": f'R$ {(saldo - valor):.2f}'
                    }
                    saldo -= valor
                    extratos.append(saque)
                    print("Saque feito com sucesso!")
                    print(f'Novo saldo: {saldo:.2f}')
                    numero_saques += 1
                else:
                    print("Não será possível sacar o valor informado, pois não há saldo suficiente.")
            else:
                print(f'Valor inserido é maior que o valor limite de R$ {LIMITE:.2f}')
        else:
            print("Número de saques diários foi excedido.")

    elif opcao == 'e':
        print("Extrato")

        if len(extratos) > 0:
            for extrato in extratos:
                pprint(extrato)
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")