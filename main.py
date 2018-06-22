from controller.slack import Slack
from controller.redis_controller import RedisController
from controller.messages import Mensagem
from config import * 

def main():
    #Object Instance
    slack = Slack(slack_token, bot_id)
    redis = RedisController("127.0.0.1", 6379, "")
    mensagem = Mensagem(slack, redis)

    #definindo comando do ADM tera que ser definido com API
    comandos_dict = {'listar aws':'listaws', 'listar usuarios':'listusers'}
    redis.push("comandos_admin", comandos_dict)
    #log("info", "Start app")
    if slack.sc:
        while True:
            for slack_message in slack.sc.rtm_read():
                
                message = slack_message.get("text")
                user = slack_message.get("user")
                for_me = slack.is_for_me(slack_message)
                if for_me:
                    try:
                       mensagem.receive_message("admin", str(user), str(message))
                    except Exception as e:
                        slack.send_message(str(e))
                        print "exception: " +str(e)
                        #log("error", "Provavel erro de conexao MYSQL "+ str(e))

    else:
        print "erro"
        #log("error", "Impossivel conectar no Slack, verificar Token")


if __name__ == '__main__':
    main()
