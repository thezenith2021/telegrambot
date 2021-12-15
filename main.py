import requests
import time
import json

class TelegramBot:
    def __init__(self):
        token = '5048649726:AAGxQc9ppdlmluUBThoRbXCAVBdwIwNYoeE'
        self.url_base = f'https://api.telegram.org/bot{token}/'
    #ligar o bot
    def Iniciar(self):
      update_id = None
      while True:
        atualizacao = self.obter__mensagens(update_id)
        mensagens = atualizacao['result']
        if mensagens:
          for mensagens in mensagens:
            update_id2 = mensagen['update_id']
            chat_id = mensagem['message']['from']['id']
            resposta = self.criar_resposta()
            self.responder(resposta,chat_id)
    # Obter mensagens
    def obter__mensagens(self,update_id):
      link_requisicao = f'{self.url_base}getUpdates?timeout=100'
      if update_id:
        link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
      resultado = requests.get(link_requisicao)
      return json.loads(resultado.content)
    # Criar uma resposta
    def criar_resposta(self):
      return 'ola eu sou apenas de teste meu sonho é ser igual aos meus primos bots do discord'
    # responder
 def responder(self,resposta,chat_id):
   # enviar
   link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
   requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()