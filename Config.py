import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("1740969", 6)
    API_HASH = os.environ.get("6b35a0c554a76cb2ad6a47f43eda4674", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("1096804830").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1096804830)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Hey [{}](tg://user?id={}). I am The Force Subscribe Bot**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn off ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @Divyansh_Choudhary**"

        "**Powered by @DcCreations**"
      ]

      START_MSG = [ "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\n\n 📣Join [Channel]("https://t.me/iGroupZoid")\n 💬Join [Support Group]("https://t.me/TheGroupZoid")\n📢 Also Join [New Channel]("https://t.me/Dccreations")\nLearn more at /help__"]
