# def is_palindrome(num):
#     """判断一个数是不是回文数"""
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num
#
#
# num=input('num=')


# print(is_palindrome(int(num)))
# import world as world
#
# s1 = r'hello, world!'
# s2 = r'\n\hello, world!\\n'
# print(s1, s2, end='')
import time

import numpy


def test70(n):
    # dp = [0] * (n + 1)
    # dp[0] = 1
    # dp[1] = 1
    # for i in range(2, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    # return dp[n]

    # if n <= 2:
    #     return n
    list1 = [0] * (n + 1)
    list1[0] = 1
    list1[1] = 2
    i = 3
    for i in range(2, n + 1):
        list1[i] = list1[i - 1] + list1[i - 2]
    return list1[n]


def test121():
    list2 = [7, 1, 5, 3, 6, 4]
    list3 = [7, 6, 4, 3, 1]
    list1 = [1, 2]
    max = 0
    count = 0
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[j] - list1[i] > max:
                max = list1[j] - list1[i]
                count = j

    if count == 0:
        print(0)
    else:
        print(count + 1)


# addsadsaddsas
# ads

# def log(func):
#     def wrapper(*args, **kw):
#         print("当前函数名: %s()" % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper()


# 1．查看项目名称，验证点：必填项，默认值为空，最大长度为200，限制字符<>$^%输入
# 2、查看增收目标，验证点：必填项，默认值为空，数字输入框，范围0.01-999.00(MUSD)，0.01-99999.00(万RMB)

def hefa(n):
    fangwei = ["A", "W", "S", "D"]
    fangxiang=""
    bushu=""
    # print(n)
    if n[0:1] in fangwei:
        # print(n)
        fangxiang=n[0:1]
        if  n[1:2].isdigit():
            if n[1:3].isdigit() and len(n)<=3 and len(n)>0:
                # print(n[1:3])
                bushu=bushu+n[1:3]
                return fangxiang+"+"+str(bushu)
            elif n[1:2].isdigit() and len(n)==2 :
                bushu=bushu+n[1:2]
                return fangxiang+"+"+str(bushu)
            else:
                return "error"
        else:
            return "error"
    else:
        return "error"


def yidong(fx,bs):
    bs=int(bs)
    if fx=="A":
        result["x"]=result["x"]-bs
        # print("")
    elif fx=="W":
        result["y"] = result["y"] + bs
    elif fx=="S":
        result["y"] = result["y"] - bs
    elif fx=="D":
        result["x"] = result["x"] + bs


def testsuibian(n):

    s = input()
    list1 = n.split(";")
    # print(list1)
    for i in list1:
        # print(i)
        h=hefa(i)
        if h!="error":
            daan=hefa(i)
            fx=daan.split("+")[0]
            bs=daan.split("+")[1]
            # print("校验通过,本次位移是%s , %s"%(fx,bs))
            yidong(fx,bs)
        else:
            continue
    print("%s,%s"%(result["x"],result["y"]))



if __name__ == '__main__':
    result = {"x":0 , "y": 0}
    # testsuibian()
    testsuibian("A10;S20;W10;D30;X;A1A;B10A11;;A10;")




