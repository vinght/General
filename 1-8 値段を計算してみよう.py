#値段を計算する
import random
apple_price = random.randint(1,3) * 100 #リンゴの単価 ただ分かりやすく変数名決めてるだけ
apple_num = random.randint(1,10)  #リンゴを買う数 以下略
print("リンゴの単価 : " + str(apple_price) + "円")
print("リンゴを買う数 : " + str(apple_num) + "個")
'''
pythonは下記の演算子が定義されている

+a            # 正数
-a            # 負数
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算
a % b         # a を b で割った余り
a ** b        # a の b 乗
a // b        # 切り捨て除算


'''

total = apple_price * apple_num
print("合計金額 : " + str(total) + "円")
