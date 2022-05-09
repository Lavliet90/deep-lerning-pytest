from faker import Faker

faker = Faker()


class PlayerLocalization:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            'nickname': self.fake.first_name()
        }

    def buil(self):
        return self.result


