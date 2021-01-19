# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:01:59 2020

@author: henri
"""

from time import sleep
from whatsapp_api import WhatsApp

wp = WhatsApp()
input("Pressione enter após escanear o QR Code")
nomes_palavras_chaves = ['Ciclano bot', 'Amelia bot', 'Sophia bot', 'Olivia bot', 'Beltrano bot', 'Fulano bot']
primeiros_nomes = [nome.split(' ')[0] for nome in nomes_palavras_chaves]
lista_produtos = ['celular', 'impressora', 'câmera', 'kindle', 'mouse', 'teclado']
for primeiro_nome, nome_pesquisar, produto in zip(primeiros_nomes, nomes_palavras_chaves, lista_produtos):
    mensagem = f'Olá {primeiro_nome}! Obrigado por comprar o produto {produto}!'
    wp.search_contact(nome_pesquisar)
    sleep(2)
    wp.send_message(mensagem)
sleep(10)
wp.driver.close()