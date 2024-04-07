#Fase 1 projeto integrador
#MENU
import sys
import time
import pandas as pd
# Começo Loading Bar
def loading_bar():
    toolbar_width = 10
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))

    for i in range(toolbar_width):
        time.sleep(0.10)  # Simulando algum processo que está sendo executado
        sys.stdout.write(".")
        sys.stdout.flush()

    sys.stdout.write("\n")
#Fim Loading Bar
    
cod=int(input("\nDigite o código do produto: ")) 
loading_bar()
print("\nRegistrado com sucesso!")

prod=str(input("\nDigite o nome do produto: "))
loading_bar()
print("\nRegistrado com sucesso!")

desc=str(input("\nDigite a descrição do produto: "))
loading_bar()
print("\nRegistrado com sucesso!")

CP=float(input("\nDigite o custo do produto em reais: "))
loading_bar()
print("\nRegistrado com sucesso!")

CF=float(input("\nDigite o custo fixo em %: "))
loading_bar()
print("\nRegistrado com sucesso!")

CV=int(input("\nDigite a comissão de venda em %: "))
loading_bar()
print("\nRegistrado com sucesso!")

IV=int(input("\nDigite o valor dos impostos em %: "))
loading_bar()
print("\nRegistrado com sucesso!")

ML=int(input("\nDigite o valor da rentabilidade em %: "))
loading_bar()
print("\nRegistrado com sucesso!")


PV=0
PV=CP/(1-((CF+CV+IV+ML)/(100)))
CA=(CP*100)/PV
RB=PV-CP
RBB=(RB*100)/PV
CFF=(PV/100)*CF
CVV=(PV/100)*CV
IVV=(PV/100)*IV
OC=((CFF)+(CVV)+(IVV))
OCC=((CF)+(CV)+(IV))
ML=((RBB)-(OCC))
MLL=((RB)-(OC))



#Criando a tabela
df=pd.DataFrame({"Descrição":["Peco de venda","Custo de aquisicao(fornecedor)",
"Receita bruta (A-B)","Custo fixo/Administrativo","Comissao de vendas","Impostos","Outros custos (D + E + F)",
"Rentabilidade", ],
                "Valor":[PV,CP,RB,CFF,CVV,IVV,OC,MLL],
                "%":["100%",CA,RBB,CF,CV,IV,OCC,ML]})

print(df)

#Definindo Rentabilidade
if ML > 20:
    print("\nO produto se encontra na faixa de lucro ALTO.")
elif ML > 10 or ML < 20:
    print("\nO produto se encontra na faixa de lucro MÉDIO.")
elif ML > 0 or ML < 10:
    print("\nO produto se encontra na faixa de lucro BAIXO.")
elif ML == 0:
    print("\nO produto se encontra em EQUILÍBRIO.")
else:
    print("\nO produto se encontra em PREJUÍZO.")