import requests
from tkinter import *

def get_price():
    req = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    req_dic = req.json()

    dolar_price = req_dic['USDBRL']['bid']
    euro_price = req_dic['EURBRL']['bid']
    BTC_price = req_dic['BTCBRL']['bid']

    text = f'''
    Dólar: {dolar_price}
    Euro: {euro_price}
    BTC: {BTC_price}
    '''

    prices["text"] = text


janela = Tk()
janela.geometry("350x350")
janela.title("Cotação atual das moedas: ")

guidance_label = Label(janela, text='Clique no botão abaixo para exibir as cotações atuais: ',)
guidance_label.grid(column=0, row=0, padx=10, pady=10)

button = Button(janela, text='Buscar cotações', command=get_price)
button.grid(column=0, row=1, padx=10, pady=10)

prices = Label(janela, text='As cotações apareceram aqui!')
prices.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()