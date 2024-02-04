import random


a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))


a, b = 6, 10
print(f'{a} * {b} = {a * b}')

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


# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)