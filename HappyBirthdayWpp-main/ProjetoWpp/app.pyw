import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib
from datetime import date, datetime


user_data = "user-data-dir=C:/Users/PICHAU/AppData/Local/Google/Chrome/User Data/Default"

def enviaImagens(mensagem = " ", imagem ="C:/Users/PICHAU/Documents/ProjetoWpp/image.jpg"):
    #esta funcao é como a enviaMensagens, apenas adiciona algumas ações a mais para o Selenium 

    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m")
    contatos_df = pd.read_excel("C:/Users/PICHAU/Documents/ProjetoWpp/Enviar.xlsx")


    chrome_options = Options()
    chrome_options.add_argument(user_data)
    navegador = webdriver.Chrome(chrome_options=chrome_options)




    navegador.get("https://web.whatsapp.com/")

    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)


    for i, pessoa in enumerate(contatos_df['Pessoa']):
        mensagem = mensagem.replace("*nome*", pessoa)
        numero = contatos_df.loc[i, "Número"]
        texto = urllib.parse.quote(f"{mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        
        if contatos_df.loc[i, "Aniversário"]==data_atual:
            navegador.get(link)
            while len(navegador.find_elements_by_id("side")) < 1:
                time.sleep(1)

            #Clica em cima do botão "Anexar"
            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span').click()
            #Encontra o input de enviar imagens e envia a imagem
            element = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
            element.send_keys(imagem)
            #Espera um pouco para carregar a imagem
            #Isto pode falhar, já que ele não espera nenhum elemento do html
            time.sleep(2)
            #Clica no botão de enviar
            navegador.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span').click()
            
            time.sleep(5)

    navegador.quit()


def enviaMensagens(mensagem = " "):

    ##Pega a data atual
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m")

    #Lê os contatos na planilha
    contatos_df = pd.read_excel("Enviar.xlsx")

    #Adiciona os dados do usário ao navegador
    #Importante para não requistar o qr code toda vez que o programa rodar
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/PICHAU/AppData/Local/Google/Chrome/User Data/Default")
    navegador = webdriver.Chrome(chrome_options=chrome_options)




    navegador.get("https://web.whatsapp.com/")

    #Espera até que o wpp tenha sido carregado completamente
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)



    for i, pessoa in enumerate(contatos_df['Pessoa']):

        #Troca *nome* pelo nome da pessoa na planilha de contatos
        mensagem = mensagem.replace("*nome*", pessoa)

        numero = contatos_df.loc[i, "Número"]

        #faz um parse no texto para ser compatível com a url
        texto = urllib.parse.quote(f"{mensagem}")

        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

        #Se a data de aniversário for a mesma de hoje, envie a mensagem
        if contatos_df.loc[i, "Aniversário"]==data_atual:
            navegador.get(link)
            while len(navegador.find_elements_by_id("side")) < 1:
                time.sleep(1)

            #Pressiona enter no campo de mensagem e a envia
            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
            time.sleep(5)
    
    navegador.quit()


def rodaPrograma(init=False):
    arquivo = open('data.txt', 'r', encoding="utf8")
    #Le o tipo de mensagem a ser enviada
    aux = arquivo.readline()
    aux = aux.split()
    tipo = aux[0]
    
    aux = arquivo.readline()
    aux = aux.split("\n")
    imagem = aux[0]

    #Le a mensagem a ser enviada
    mensagem=arquivo.read()

    #Pega a hora atual
    agora = datetime.now()
    agora = agora.strftime("%H")

    ##Executa apenas se a hora atual for meia noite ou se estiver inciando
    if(agora=="10" or init==True):
        if(tipo=="texto"):
            enviaMensagens(mensagem)
        elif(tipo=="imagem"):
            enviaImagens(mensagem, imagem)

    arquivo.close()


#Executa o programa uma vez ao iniciar

while True:
    rodaPrograma()
    time.sleep(3600)