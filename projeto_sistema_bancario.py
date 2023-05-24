from datetime import datetime

# função para exibir o menu: apenas por organização visual
def menu() -> None:
    print('''===BEM VINDO AO BANCO NEXT===
Escolha alguma das opções abaixo:
[S] Sacar
[D] Depositar
[E] Extrato
[Q] Sair 
    ''')

# Declaração de variáveis
data = datetime.now()                    # Obter informação de data e hora do sistema operacional
saldo = 0                                # Saldo Acumulado
extrato = ""                             # Armazenar as informações das ações realizadas durante o uso
QTD_MAX_SAQUE = 3                        # Constante para o limite máximo da quantidade de vezes que é possível o saque
LIMITE_VALOR_SAQUE = 500                 # Limite máximo de valor que é possível sacar diáriamente
Contador_saque = 0                       # Contar quantas vezes o saque foi realizado


while True:
    menu()
    # variável para obter a opção escolhida pelo usuário
    op = str(input("Digite aqui sua opção: ")).strip().upper()

    # controle de decisão da opção escolhida
    while op not in 'DdSsEeQq':

        print("Opção inexistênte, tente novamente...")
        op = input("Digite aqui sua opção: ")

    # Opção para sair do programa
    if op in 'Qq':

        break

    # Opção de Saque
    if op in 'Ss':

        if Contador_saque < QTD_MAX_SAQUE:                         # primeiro é feita a checagem para saber se foi realizado o número máximo de saques diários

            op_de_retorno = 0                                      # A variável permanece com valor "0" ou "falso" para o saque ser efetuado, caso mude pra 1, houve algum erro.

            saque = float(input("Digite o valor que deseja sacar: "))              # recebe o valor de saque do usuário.

            # Controle para saber se o valor de saque não é maior do que o saldo disponível
            while saque > saldo:
                print("Saldo insuficiente, deseja retornar ao menu?\n[1] Sim\n[0] Não")
                op_de_retorno = int(input("Digite sua opção: "))
                
                # Caso ocorra essa tentativa, o flag "op_de_retorno" passa a valer 1 indicando o erro, enquanto o valor não atender as condições, o saque não será efetuado.
                if op_de_retorno == 1:
                    break
                else:
                    saque = float(input("Digite o valor que deseja sacar: "))


            if saque <= saldo and saque <= 500:                                     # Caso esteja tudo de acordo, o saque será efetuado.
                saldo -= saque
                print("Saque efetuado com sucesso!")
                Contador_saque += 1
                extrato += f"Valor do saque: R$ {saque:.2f}\nData e hora: {data}\n"
            else:
                while saque <= 0 or saque > 500:                                               # Caso o saque for negativo ou nulo retorna-rá a mensagem de valor inválido e o flag vira 1 caso volte ao menu e saque não é efetuado.

                    if saque == 0:
                        print("Valor inválido, deseja retornar ao menu?\n[1] Sim\n[0] Não")
                        op_de_retorno = int(input("Digite sua opção: "))
                        if op_de_retorno == 1:
                            break
                        else:
                            saque = float(input("Digite o valor que deseja sacar: "))
                    else:                                                                   # Caso o valor exceda o limite de 500 reais

                        print(f"Valor do saque excedeu o limite de R${float(LIMITE_VALOR_SAQUE):.2f}, deseja retornar ao menu ou sacar novamente?\n[1] MENU\n[0] SAQUE")
                        op_de_retorno = int(input("Digite sua opção: "))

                        if op_de_retorno == 1:
                            break
                        else:
                            saque = float(input("Digite o valor que deseja sacar: "))

                if op_de_retorno == 0:                   # Caso o flag continuar em "0" é sinal que os erros foram corrigidos e os valores informados corretamente
                    saldo -= saque
                    print("Saque efetuado com sucesso!")
                    Contador_saque += 1
                    extrato += f"Valor do saque: R$ {saque:.2f}\nData e hora: {data}\n"

        else:
            print("Limite de saque diário excedido!\nRetorne novamente amanhã.")                      # Caso o limite de saque tenha excedido essa mensagem será acionada ao selecionar a opção de saque.

    # Opção de Deposito
    elif op in 'Dd':
        
        depositar = float(input("Digite o valor que deseja depositar: "))

        # Controle para saber se o valor informado pelo usuário é compatível 
        while depositar <= 0:

            print("Valor inválido, deseja retornar ao menu?\n[1] Sim\n[0] Não")
            op_de_retorno = int(input("Digite sua opção: "))
            
            # A decisão de retorno é controlada pela variavel "op_de_retorno" para evitar que valores negativos e nulos estejam presentes
            if op_de_retorno == 1:
                break
            else:
                depositar = float(input("Digite o valor que deseja depositar: "))

        # caso o valor seja coerênte o depósito será aceito e registrado no extrato com o valor, data e hora.
        if depositar > 0:
            saldo += depositar
            print("Depositado com Sucesso!")
            extrato += f"Valor do deposito: R$ {depositar:.2f}\nData e hora: {data}\n"

    # Opção de Extrato
    else:
        print("\nApresentando seu extrato...\n")
        print(extrato)
    