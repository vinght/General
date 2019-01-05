# 西暦年から平成年を求める
'''
import datetime
seireki = datetime.date.today().year
print('西暦' + str(year) + '年')'''

#西暦年 - 1988 =
year = 2018
Heisei = year - 1988
print(Heisei)
if year < 1988:
    print("平成")



'''
year = 1926
Shouwa = year - 1925
print(Shouwa)
#昭和まで、1987年までが昭和
'''


#print(JP_year)

'''
# 西暦を昭和年に変換
import random
seireki = random.randint(1926, 1988) #西暦年
print("西暦" + str(seireki) + "年は", end = "")

# 昭和年を計算
showa = seireki - 1925 #←いじったのここだけ、算数の問題じゃねえかよこれぇ！！！
# 昭和年を出力
print("昭和" + str(showa) + "年です。")
'''