from controller.slack import Slack
from controller.redis_controller import RedisController

import ast

class Mensagem():
    slack = None
    redis = None
    message = None
    user = None

    def __init__(self, Slack, Redis):
        self.slack = Slack
        self.redis = Redis
        
    def receive_message(self, auth, user, message):
        #clean message
        self.message = " ".join((message.split(" "))[1:])
        self.user = user
        if auth == "admin":
            comandos = ast.literal_eval(self.redis.pop("comandos_admin"))
            if self.message == "help":
                print "entrei"
                for resposta, execucao in comandos.items():
                    self.slack.send_message("<@"+str(self.user) + "> " + str(resposta))
            elif self.message in comandos:
                #instancia o metodo que eu quero chamar baseado na string
                try:
                    getattr(self, comandos[self.message])()
                except:
                    self.slack.send_message("<@"+str(self.user) + "> " + str("Metodo ainda nao implementado"))
            else:
                self.slack.send_message("<@"+str(self.user) + "> " + str("Voce deveria tentar help"))  
                                  
    def listusers(self):
        print "entrei list users"
        self.slack.send_message("<@"+str(self.user) + "> " + str("Funcionou"))
