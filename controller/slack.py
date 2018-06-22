from slackclient import SlackClient

class Slack():

    token = None
    sc = None
    bot_id = None
    channel = None

    def __init__(self, token, bot_id):
        self.token = token
        self.bot_id = bot_id
        self.sc = SlackClient(self.token)
        self.sc.rtm_connect()
        #log("info", sc)
    
    def send_message(self, message):
        self.sc.rtm_send_message(self.channel, message)
    
    def is_for_me(self, event):
        type = event.get('type')
        try:
            if type and type == 'message':
                text = event.get('text')

                self.channel = event.get('channel')
                if str(self.bot_id) in str(text):
                    #log("info", "is_for_me -- text: %s , bot_id: %s and channel: %s " %(text, bot_id, str(channel)))
                    return True
        except:
            return None