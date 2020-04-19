import random

# random.sample(str,n)：从str中随机取出n个字符组成一个list。
for i in range(6):
    print(''.join(random.sample('1234567890',8))+'@qq.com')