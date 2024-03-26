#Calculo do lucro fase 1 PI.versão_teste
print(f"Calculo do lucro de um produto!")
cod=int(input("Digite o código do produto: "))
prod=str(input("Digite o nome do produto: "))
desc=str(input("Digite a descrição do produto: "))
CP=float(input("Digite o custo do produto em reais: "))
CF=float(input("Digite o custo fixo em %: "))
CV=int(input("Digite a comissão de venda em %: "))
IV=int(input("Digite o valor dos impostos em %: "))
ML=int(input("Digite o valor da rentabilidade em %: "))
PV=0
PV=CP/(1-((CF+CV+IV+ML)/(100)))
PPV=
