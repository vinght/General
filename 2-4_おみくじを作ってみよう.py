# おみくじを作る
# 比較演算子 == > < >= <= !=
# 大吉  中吉  小吉  凶  大凶
import random
number = random.randint(1,20)

if number == 1:
    print('大吉です')
elif number <= 3: #2,3
    print('中吉です')
elif  number <= 6: #4,5,6
    print('小吉です')
elif number <= 10: #7,8,9,10
    print('凶です')
else:
    print('大凶です') #それ以外は大凶
print(number)

'''
正直、比較演算子の扱いがしっかりできてれば楽々
'''