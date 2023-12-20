import random


def random_phone_number():
    prefix = [57, 12, 13, 21, 95, 18]
    
    start_digits = "8" + str(random.choice(prefix))
    middle_digits = str(random.randint(10000000, 99999999))
    random_number = start_digits + middle_digits

    return str(random_number)


def random_single_number():
    return str(random.randint(0, 9))

