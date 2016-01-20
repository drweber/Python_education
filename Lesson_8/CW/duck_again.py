class Duck:
    def __init__(self, name):
        self.name = name
        print("Hello, {}".format(self.name))

    def __del__(self):
        print("Bye-bye, {}".format(self.name))

    def say (self, msg):
        print ('{} said {}'.format(self.name,msg))

if __name__ == "__main__":
    d = Duck(name="Donald Duck")
    d.say ("'Yep'")
    del d
    print("after all...")