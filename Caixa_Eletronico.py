"""
Projeto que simula a criação e execução de um caixa eletrônico
"""

from tkinter import *
from PIL import Image, ImageTk
import time

def saldo():
    conclusao['text']= f'Seu saldo atual é R$ {saldoAtual}'
    janela.update()
    normalizar()

def saque():
    global saque_pagar
    saque_pagar = True
    conclusao['text'] = 'Quanto deseja sacar?'
    botaoValores()

def botaoValores():
    botao1['text'] = '50'
    botao1['command']= saque50
    botao2['text']= '100'
    botao2['command']= saque100
    botao3['text'] = '500'
    botao3['command']= saque500
    botao4['text']= '1000'
    botao4['command']= saque1000
    botao5['text'] = '5000'
    botao5['command']= saque5000
    botao6['text']= 'Confirmar\nSaque'
    botao6['command']= confirmarSaque
    janela.update()

def saque50():
    global saqueTotal
    saqueTotal += 50
    conclusao['text'] = f'Valor: R$ {saqueTotal}'
    janela.update()

def saque100():
    global saqueTotal
    saqueTotal += 100
    conclusao['text'] = f'Valor: R$ {saqueTotal}'
    janela.update()

def saque500():
    global saqueTotal
    saqueTotal += 500
    conclusao['text'] = f'Valor: R$ {saqueTotal}'
    janela.update()

def saque1000():
    global saqueTotal
    saqueTotal += 1000
    conclusao['text'] = f'Valor: R$ {saqueTotal}'
    janela.update()

def saque5000():
    global saqueTotal
    saqueTotal += 5000
    conclusao['text'] = f'Valor: R$ {saqueTotal}'
    janela.update()

def confirmarSaque():
    global saqueTotal,saldoAtual,saque_pagar
    if saqueTotal > saldoAtual:
        conclusao['text'] = 'Saldo insuficiente!'
        saqueTotal = 0
    else:
        saldoAtual -= saqueTotal
        if saque_pagar:
            conclusao['text'] = f'Saque de R$ {saqueTotal} realizado com sucesso!'
        else:
            conclusao['text'] = f'Pagamento de R$ {saqueTotal} realizado com sucesso!'
        saqueTotal = 0
    janela.update()
    time.sleep(1)
    normalizar()

def normalizar():
    time.sleep(1)
    conclusao['text'] = 'Deseja realizar alguma operação?'
    botao1['text'] = 'Saldo'
    botao1['command'] = saldo
    botao2['text'] = 'saque'
    botao2['command'] = saque
    botao3['text'] = 'Pagar\nConta'
    botao3['command'] = pagar
    botao4['text'] = 'Deposito'
    botao4['command'] = deposito
    botao5['text'] = 'Desb.\nCelular'
    botao5['command'] = desbloquear
    botao6['text'] = 'Sair'
    botao6['command'] = sair
    janela.update()

def pagar():
    global saque_pagar
    conclusao['text'] = 'Qual o valor do pagamento?'
    saque_pagar = False
    botaoValores()

def deposito():
    global deposito_celular, caixa
    if deposito_celular:
        conclusao['text'] = 'Qual o valor a ser depositado?'
    else:
        conclusao['text'] = 'Digite o número do celular'
    botao1['state'] = DISABLED
    botao2['state'] = DISABLED
    botao3['state'] = DISABLED
    botao4['state'] = DISABLED
    botao5['state'] = DISABLED
    botao6['text'] = 'Confirmar'
    botao6['command'] = confirmarDeposito
    caixaTexto = Entry(janela, font= 'Arial 15')
    caixaTexto.grid(column = 1, row =5)
    caixa = caixaTexto

def confirmarDeposito():
    global caixa, saldoAtual,deposito_celular
    if caixa.get().isnumeric():
        valorDeposito = int(caixa.get())
        if deposito_celular:
            saldoAtual += valorDeposito
            conclusao['text'] = f'O valor de R$ {valorDeposito} foi depositado com sucesso!'
            time.sleep(1)
        else:
            conclusao['text'] = f'O número {valorDeposito} foi cadastrado com sucesso!'
            time.sleep(1)
    else:   #caso seja digitado uma letra ao invés de um número
        if deposito_celular:    #True para depósito
            conclusao['text'] = 'Valor inválido!'
        else:   #False para desbloquear celular
            conclusao['text'] = 'Valor inválido!'
    deposito_celular = True
    caixa.destroy()
    janela.update()
    botao1['state'] = NORMAL
    botao2['state'] = NORMAL
    botao3['state'] = NORMAL
    botao4['state'] = NORMAL
    botao5['state'] = NORMAL
    normalizar()


def desbloquear():
    global deposito_celular
    deposito_celular = False
    deposito()

def sair():
    quit()

janela = Tk()

janela.title('Caixa Eletrônico')
janela.geometry('500x380')
janela.configure(bg='blue')

saldoAtual = 5000
saqueTotal = 0
saque_pagar = True  #caso seja falso será pagamento, caso verdadeiro, será saque
deposito_celular = True #True para depósito e False para desbloqueio de celular
caixa = None
#nome= input('Nome: ')
nome = 'Bart'

introducao = Label(janela, text = f'Bem-vindo(a) ao Caixa Eletrônico, senhor(a) {nome.title()}', font=1)
introducao.grid(column=1,row=0, padx=5,pady=10) #padx é a distância de outros objetos no eixo X, pady é o mesmo no eixo Y

img = ImageTk.PhotoImage(Image.open('bancoImagem.png')) #aqui é para poder usar e armazenar a imagem como uma variável
imagem = Label(janela, image=img)   #sempre passamos primeiro o local onde será executado a Label, nesse caso é janela
imagem.grid(column=1,row=2)

botao1 = Button(janela, text='Saldo',command=saldo, height=3,width=8)
botao1.grid(column=0,row=1,padx=3,pady=1)

botao2 = Button(janela,text='Saque', command=saque, height=3,width=8)
botao2.grid(column=0,row=2,padx=3,pady=1)

botao3 = Button(janela,text='Pagar\nConta',command=pagar,height=3,width=8)
botao3.grid(column=0,row=3,padx=3,pady=1)

botao4 = Button(janela,text='Depósito',command=deposito,height=3,width=8)
botao4.grid(column=2,row=1,padx=3,pady=1)

botao5 = Button(janela,text='Desb.\nCelular',command=desbloquear,height=3,width=8)
botao5.grid(column=2,row=2,padx=3,pady=1)

botao6 = Button(janela,text='Sair',command=sair,height=3,width=8)
botao6.grid(column=2,row=3,padx=3,pady=1)

conclusao = Label(janela, text='Deseja realizar alguma operação?', font=1)
conclusao.grid(column=1,row=4,padx=10,pady=15)

janela.mainloop()


