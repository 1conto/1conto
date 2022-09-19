import pandas as pd
import datetime as dt
import os

def olha_contas(x):
    hoje = dt.date.today()
    delta = dt.timedelta(days= x)
    dia = hoje+delta
    ahhhh = pd.to_datetime(df['Data'])
    soma = 0
    for item in range(0, len(ahhhh)):
        if df['Data'][item] <= dia:
            print ('\nVocê tem uma conta de vencimento dia {} no valor de {}'.format(df['Data'][item].strftime('%d/%m/%Y'),df['Valor'][item]))
            soma = soma + float(df['Valor'][item])
    if soma != 0:
        print('\nA soma das suas contas com vencimento nos próximos {} dias é de R$ {}'.format(x, round(soma,2)))
    else:
        print('\nNão tem contas para vencimento nos próximos {} dias'.format(x))
def soma_boletos():
    ahhhh = pd.to_datetime(df['Data'])
    soma=0
    for i in range(0, len(ahhhh)):
        soma = soma+df['Valor'][i]
    return soma

"""def adiciona_boletos():
    Data=input('digite a data')
    datafra = pd.DataFrame({'Data': [Data], 'Valor': [Valor]})
    return datafra"""

def enter():
    input('OK-Enter')
    os.system('cls') or None

if __name__ == '__main__':
    df = pd.read_excel(r'C:/Users/User/Desktop/contas.xlsx')
    olha_contas(10)
    soma2 = round(soma_boletos(), 2) 
    enter()
    while 1:
        k=input('Qual ação vc quer fazer??\n1. Consultar a planilha de boletos.\n2. Colocar uma conta como paga.\n3. Adicionar um boleto na planilha.\n4. Soma dos valores dos boletos.\n5. Olhar contas dos próximos dias.\nSair/Quit. Fecha o programa\n')
        k=k.lower()
        if k == 'sair' or k=='quit':
            break
        if k == '1':
            print(df.sort_values('Data'))
            enter()
        elif k == '2':
            j= input('Qual conta vc pagou??')
            enter()
        elif k == '3':
            f = input('olá')
            enter()
        elif k == '4':
            print('A soma dos seus boletos é de R${}'.format(soma2))
            enter()
        elif k == '5':
            numb = int(input('Olhar vencimento nos próximos dias. \nDigite a quantidade de dias: \n'))
            olha_contas(numb)
            enter()
        else: 
            os.system('cls') or None
            print('Valor inválido, por favor insira um valor válido, ou digite sair ou quit para fechar o programa\nOK-Enter')