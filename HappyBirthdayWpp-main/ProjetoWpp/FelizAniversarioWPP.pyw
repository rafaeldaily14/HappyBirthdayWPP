import PySimpleGUI as sg

def textoPorImagem():
    f = open("data.txt","r", encoding="utf8")
    lines = f.readlines()
    f.close()

    f = open("data.txt","w", encoding="utf8")

    for line in lines:
        if line!="texto"+"\n":
            f.write(line)
        else:
            f.write("imagem\n")


    f.close()

def imagemPortexto():
    f = open("data.txt","r", encoding="utf8")
    lines = f.readlines()
    f.close()

    f = open("data.txt","w", encoding="utf8")

    for line in lines:
        if line!="imagem"+"\n":
            f.write(line)
        else:
            f.write("texto\n")


    f.close()

def trocaMensagem(mensagem = " "):
    f = open("data.txt","r", encoding="utf8")
    line = f.readline()
    line2 = f.readline()
    f.close()

    f = open("data.txt","w", encoding="utf8")
    f.write(line)
    f.write(line2)
    f.write(mensagem)
    f.close()

def trocaImagem(caminho):
    f = open("data.txt","r", encoding="utf8")
    line1 = f.readline()
    line2 = f.readline()
    resto = f.readlines()
    f.close()

    f = open("data.txt","w", encoding="utf8")
    f.write(line1)
    f.write(caminho+"\n")
    for line in resto:
        f.write(line)


f = open("data.txt","r", encoding="utf8")
# lines = f.readlines()
tipo = f.readline().replace("\n","")
imageDir = f.readline().replace("\n","")
mensagem= f.readline()


sg.theme('Dark')   
fonth1 = 18
fontp = 12
layout = [  [sg.Text('Feliz Aniversario WhatsApp: ', font=("Arial", fonth1))],
            [sg.Text()],
            [sg.Text('Tipo de mensagem atual: ' + tipo, key = '_text1_', font=("Arial", fontp))],
            [sg.Text()],
            [sg.T('Source Folder')],
            [sg.In(imageDir,key='input')],
            [sg.FileBrowse(target='input', file_types=(("ALL Files",".jpg"),)), sg.Button('Atualizar imagem', font=("Arial", fontp))],
            [sg.Text('Nova mensagem: ', font=("Arial", fontp))],
            [sg.Multiline(mensagem,size=(50, 5), key='textbox')],
            [sg.Radio('Imagem', "RADIO1", font=("Arial", fontp),key="r1"), sg.Radio('Texto', "RADIO1", font=("Arial", fontp),key="r2")],
            [sg.Button('Atualizar', font=("Arial", fontp)), sg.Button('Cancel', font=("Arial", fontp))]]
            

f.close()

window = sg.Window('Aproximação funcional', layout)

while True:
    event, values = window.read()
    print(values)

    
    if event == sg.WIN_CLOSED or event=="Cancel": 
        break
    if(event == 'Atualizar'):
        trocaMensagem(values['textbox'])
        if(values["r1"]==True):
            textoPorImagem()
        else:
            imagemPortexto()
        f = open("data.txt","r", encoding="utf8")
        tipo = f.readline().replace("\n","")
        window['_text1_'].Update('Tipo de mensagem atual: ' + str(tipo))
        f.close()
    elif(event=="Atualizar imagem"):
        trocaImagem(values['input'])
        f = open("data.txt","r", encoding="utf8")
        tipo = f.readline().replace("\n","")
        window['_text1_'].Update('Tipo de mensagem atual: ' + str(tipo))
        f.close()



window.close()
