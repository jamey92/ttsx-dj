import random


def get_ticket():
    ticket = ''
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    for _ in range(50):
        ticket += random.choice(s)
    return ticket
