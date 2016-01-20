#!/usr/bin/python
# coding=utf-8

"""

"""
import json

class Player(object):
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        self.sessions = []
        self.wallet = {}

    def load_money(self):
        pass

    def as_dict(self):
        data_to_save = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions,
            "wallet": self.wallet
        }
        return data_to_save

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        self.email = object_as_dict["email"]
        self.password = object_as_dict["password"]
        self.session = object_as_dict["session"]
        self.wallet = object_as_dict["wallet"]
        return object_as_dict

    def login(self):
        pass

    def logout(self):
        pass

    def give_money(self, code, amount):
        pass

    def take_money(self, code, amount):
        pass

class Moderator(Player):
    pass

class Administrator(Moderator):
    pass

class Session(object):
    def __init__(self, start_time, finish_time):
        self.start_time = start_time
        self.finish_time = finish_time
        self.id = 'generate.id'

class Money(object):
    def __init__(self, code, ammount):
        self.code = code
        self.ammount = ammount

MONEY_CODE_1 = 'gems'
MONEY_CODE_2 = 'woods'
MONEY_CODE_3 = 'coins'

if __name__ == "__main__":
    player1 = Player('chukcha','chukcha@mail.ref','chukcha_ne_durak')
    gems = Money(MONEY_CODE_1,0)
    wood = Money(MONEY_CODE_2,0)
    coins = Money(MONEY_CODE_3,0)
    
    player1.wallet = {MONEY_CODE_1: gems, MONEY_CODE_2: wood, MONEY_CODE_3: coins}
    
 