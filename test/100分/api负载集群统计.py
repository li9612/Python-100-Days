num=input()
num=int(num)
list1=list()
x=0
dic = {}
list_s={}

def  add(*args):
    a=args
    return
#拆字符
# def chai(str):
#     list_s=str.split("/")
#     return list_s

#按照/拆分字符串，去掉无用元素
for x in range(num):

    a=input()
    b=a.split("/")
    b.pop(0)
    c=b
    list1.append(c)

    # print(chai(list1[x]))
    # dic.update({add(list1(a)):()})

print(list1)
#把拆分后的数组加到字典里,字典格式为  路径：（层数，次数）
# list1_num=len(list1)
# for x in range(list1_num):
#     dic.update(chai(list1[x]))

for x in range(num):
    dep = 0
    # depstr=string(dep)
    # depnum=dep+1
    # if dic.keys([list1[dep]+""+dep]):
    print(list1(dep))
    # dic[list1[dep]+""+str(dep)]=dep






print(dic)






