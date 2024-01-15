import toolTest

def test6():
    keys = ['1001', '1002', '1003']
    values = ['骆昊', '王大锤', '白元芳']
    d = dict(zip(keys, values))
    print(d)


    toolTest.bar()


def gcd(x, y):
    # (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


if __name__ == '__main__':
    print(gcd(18,15))



import sys



# list1= ['北京','香港','qwe','asd','zxc']
# a=random.sample(list1,2)
#
# b=random.sample(list1,1)
# print(a)
# print(b)

# def roll_dice(n=2):
#         """摇色子"""
#         total = 0
#         for _ in range(n):
#             total += randint(1, 6)
#         return total
#
# def add(a=0, b=0, c=0):
#     """三个数相加"""
#     return a + b + c
#
#     # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
#     # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
#     # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


# if __name__ =="__main__":
#     add()