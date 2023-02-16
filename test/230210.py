import random


def huiwen(x):
    m=x
    t=0
    while m>0:
        t=t*10+m%10
        m//=10
    return x==t

def sushu(num):
    for factor in range(2, int(num ** 0.5)+1):
        if num % factor == 0:
            return False
    return True
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True



if __name__ =="__main__":
    num = int(input('请输入正整数: '))
    # if is_prime(9):
    if sushu(num)and huiwen(num):
        print("yes")
    else:
        print("no")
