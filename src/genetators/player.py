from src.enums.user_enums import Statuses

from src.genetators.player_localization import PlayerLocalization

class Player:

    def __init__(self):
        self.result = {}
        self.reser()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.result['avatar'] = avatar

    def reser(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result['localize'] = {
                'en': PlayerLocalization('en_US').buil(),
                'ru': PlayerLocalization('ru_RU').buil(),
        }
        return self

    def build(self):
        return self.result
