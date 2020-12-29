import random
import string

pre_fix = ['WORK']
suf_fix = ['_TAG']
nums = random.randint(100,999)

def work_id():
    result =random.choice(pre_fix)
    results = random.choice(suf_fix)

    return f'{result}130_{nums}{results}'