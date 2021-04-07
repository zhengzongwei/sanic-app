import random
import time
import os


def generate_smscode(lengh: int = 6) -> int:
    """
    generate sms code
    :return:
    """
    code = ''
    for i in range(lengh):
        num = random.randint(0, 9)
        code += str(num)
    return int(code)


def execute_time(func):
    """
    compute function execute time
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_return = func(*args, **kwargs)
        end_time = time.time()
        formet_str = ("[%s] execute time: %s " % (func.__name__, end_time - start_time))
        print(formet_str)
        os.system("echo %s >> %s-esexute-time" % (formet_str, func.__name__))
        return func_return

    return wrapper


def now_time(nowtime: int = None) -> str:
    """
    formatting time
    """
    if nowtime is None:
        nowtime = time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(nowtime))


def now_timestrap():
    return time.time()


def timestrap(str_time: str) -> int:
    """
    formatting time to timestrap
    """
    return time.mktime(str_time, "%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print(generate_smscode())
