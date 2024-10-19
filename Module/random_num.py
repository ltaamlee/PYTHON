import random

def gen_num(n, Min, Max):
    return [random.randint(Min, Max) for _ in range(n)]