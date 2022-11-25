# HappyBirthdayWpp
Uma automação com o navegador que envia uma mensagem no wpp no dia do aniversário



Os contatos devem ser adicionados na planilha "Enviar", em que o número de telefone deve respeitar o padrao internacional ex.: "5564999999999".

As datas de aniversário devem respeitar o padrão XX/XX.

o programa FelizAniversarioWPP é uma interface que permite mudar a mensagem, a imagem escolhida (caso queira enviar uma imagem) e o tipo de mensagem, se é apenas texto ou se contém imagem.

O código utiliza o Selenium para realizar a automação, sendo o navegador utilizado o Chrome. Você deve baixar o chromedrive em https://chromedriver.chromium.org/downloads e o instalar na mesma pasta onde está instalado o pyhton para que o progama rode com êxito.

Para que o programa não requisite toda vez o qrCode, você deve passar as configurações do seu navegar, para isso, mude o diretorio presente na variável "user_data" no início do código.

O progama sempre manda as mensagens as 10 da manhã do horário local.

Os XPath podem mudar de acordo com atualizações do própio whatsapp web, então certifique-se de alter os XPath do código para que o progama funcione.
