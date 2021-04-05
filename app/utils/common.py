import random


def generate_smscode(lengh:int=6)->int:
    """
    generate sms code
    :return:
    """
    code = ''
    for i in range(lengh):
        num = random.randint(0, 9)
        code +=  str(num)
    return int(code)



if __name__ == '__main__':

    print(generate_smscode())