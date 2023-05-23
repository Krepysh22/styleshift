from pydantic import BaseSettings


class TgSettings(BaseSettings):
    api_hash = 'ed7f50a46841583d9a6bbd35ee24236a'
    app_id = '23610502'
    bot_token = '2038428887:AAHj12f_os1ulzNRh3zpYAlGICHmC6qEokM'
    list_of_send_to = [460788585, 1074944366]

settings = TgSettings()

