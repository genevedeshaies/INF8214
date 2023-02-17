from random import randint
from time import sleep, time

def decorateur(fonction):
    def fonctionmodifiee(*argv):
        sleep(randint(1,3))


def hello(nom="world"):
    print(time())
    sleep(randint(1,3))
    print(time)