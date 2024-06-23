saldo = 1000
saque = 0
deposito = 0
contador_saque = 0
numero_de_saques = []
numero_de_depositos = []

while contador_saque < 3:
    operacao = input('Você deseja realizar um saque ou deposito? ').lower().strip()

    if operacao == 'saque':
        novo_saque = int(input('Informe quanto deseja sacar: '))
        if novo_saque > 500:
            print('Valor excede o limite diário de saque')
        elif novo_saque > saldo:
            print('Saldo insuficiente')
        elif novo_saque <= 0:
            print('Valor de saque inválido')
        else:
            saque += novo_saque
            contador_saque += 1
            numero_de_saques.append(novo_saque)
            saldo -= novo_saque
            print('Saque realizado com sucesso!')

    elif operacao == 'deposito':
        novo_deposito = int(input('Informe quanto deseja depositar: '))
        if novo_deposito <= 0:
            print('Valor de depósito inválido')
        else:
            deposito += novo_deposito
            numero_de_depositos.append(novo_deposito)
            saldo += novo_deposito
            print('Depósito realizado com sucesso!')

    else:
        print('Operação inválida')

# Exibindo o extrato
print("\n--- Extrato ---")
print("Saques realizados:")
for saque in numero_de_saques:
    print(f"- R$ {saque:.2f}")

print("\nDepósitos realizados:")
for dep in numero_de_depositos:
    print(f"- R$ {dep:.2f}")

print(f"\nSaldo final: R$ {saldo:.2f}")
