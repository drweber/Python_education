#!/usr/bin/python
# coding=utf-8

"""

"""
import json

class Player(object):
    def __init__(self, name=None, email=None, password=None, session=[], wallet={}):
        self.name = name
        self.email = email
        self.password = password
        self.session = session
        self.wallet = wallet

    def as_dict(self):
        data_to_save = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "session": self.session,
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

    def give_money(self):
        pass

    def take_money(self):
        pass

class Moderator(Player):
    pass

class Administrator(Moderator):
    pass

class Session(object):
    def __init__(self, start_time=None, finish_time=None):
        self.start_time = start_time
        self.finish_time = finish_time

class Money(object):
    def __init__(self, code=None, ammount=0):
        self.code = code
        self.ammount = ammount

if __name__ == "__main__":
    player1 = Player('chukcha','chukcha@mail.ref','chukcha_ne_durak',Session,{})
    jems = Money('jems',0)
    wood = Money('wood',0)
    coins = Money('coins',0)
