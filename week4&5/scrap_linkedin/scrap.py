# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ciência-de-dados-vagas/?position=1&pageNum=0'

if __name__ == '__main__':
    # Criando instância do Chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    # Acessando Linkedin
    driver.get(URL_LINKEDIN_DS)
    
    #Pegando lista de resultados de vagas
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricao = []
    
    #Iniciar loop em cima de todos os resultados
    while(True):
        # Loop para coletar descrições de dados
        for r in resultados[len(lista_descricao):]:
            r.click() # Clica na descrição
            sleep(2)
            try:
                # Pegar elemento com a descrição
                descricao = driver.find_element_by_class_name('description')
                # Anexar texto da descrição na lista
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
            
        resultados = resultados = driver.find_elements_by_class_name('result-card')
        
        # Critério de saída do While
        if len(lista_descricao) == len(resultados):
            break
        
    # Salvar descrições de vagas
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt', 'w') as f:
        f.write(descricao_salvar)
    
    # Fecha o Chrome
    driver.quit()
    