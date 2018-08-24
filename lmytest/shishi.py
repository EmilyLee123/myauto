# import random
#
# input = "测试课程"
# print(input)
#
# r = random.randint(0, 999999)
# print(r)
import random

id = random.randint(0, 5)
print(id)
print(type(id))
list = ['123', '874798', '1', '2', '3', '4', '5']
#list.append(id)
print(list)
print(type(list[0]))
if str(id) in list:
    print('成功')
else:
    print('失败')