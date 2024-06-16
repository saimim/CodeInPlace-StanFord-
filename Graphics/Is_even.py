def main():
    for i in range(10,20):
        if oddv1(i):
            print(i, 'odd')
        else:
            print(i,'even')

def oddv1(i):
    while i>2:
        i = i-2
    if i==2:
        return False
    
def oddv2(i):
    reminder = i%2
    if reminder == 1:
        return True
    else:
        return False

def is_odd(i):
    reminder = i%2
    to_return = reminder == 1
    return to_return