import random
import string

pre_fix = ['ANC']
nums = random.randint(100,999)

def staff_new_id():
    result =random.choice(pre_fix)

    return f'{result}130{nums}'