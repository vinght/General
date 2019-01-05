# 西暦年と平成年の対応表を作る
# 1989年から2016年までをループで出力
# ループ内で、各西暦年を平成年に変換

for year in range(1989,2017):
    print('西暦' + str(year) + '年は', end = "") #end = ""は改行すんなって指令。覚えとけ
    year = year - 1988
    print('平成' + str(year) + '年です')


    # 西暦年と昭和年の対応表
# 1926年から1988年までをループで出力
# ループ内で、各西暦年を昭和年に変換
for year in range(1926,1989):
    print('西暦' + str(year) + '年は', end ="")
    SW_year = year - 1925
    print('昭和' + str(SW_year) + '年です')



# 特定期間の西暦年と昭和年の対応表を作る
# 1行目：開始年
# 2行目：期間
# 昭和年 = 西暦年 - 1925
# 出力：西暦XXXX年は昭和YY年です
num1 = int(input())
num2 = int(input())
for num1 in range(num2): #おかしいのここ
    print(num1)
    print('西暦' + str(num1) + '年は',end = "")
    SW_year = num1 - 1925
    print('昭和' + str(SW_year) + '年です')


num1 = int(input())
num2 = int(input())
for num2 in range(num1,num1 + num2): #おかしいのここ
    print('西暦' + str(num1) + '年は',end = "")
    SW_year = num1 - 1925
    print('昭和' + str(SW_year) + '年です')


# 正解
num1 = int(input())
num2 = int(input())
for num2 in range(num1,num1 + num2): #おかしいのここ
    print('西暦' + str(num1) + '年は',end = "")
    SW_year = num1 - 1925
    print('昭和' + str(SW_year) + '年です')
    num1 = num1 + 1
    
test = 1975 - 1925
print(test)
test = 1976 - 1925
print(test)
test = 1977 - 1925
print(test)

# 詰まったときは直入力して細かく見ていくと答えがわかる、変数で考えるからわかんなかったら数字で考えろ

'''
num1 = 1975
num2 = 10


num1 = input()
num2 = int(input())
SW_year = num2 - num1
for num1 in range(num2): #おかしいのここ
    print('西暦' + str(num1) + '年は',end = "")
    SW_year = num2 - num1
    print('昭和' + str(SW_year) + '年です')'''