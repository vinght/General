'''
for number in range(10):
    if number == 5:
        continue
    print(number)
# このcontinueは
# number == 5
# の時だけスキップするって文です。
'''

# 実践演習
# while文を利用して10から５0までの間の偶数のみを出力せよ（目標１５分）
'''number = 10
while (number <= 50):
    if number % 2 == 0:
        print(number)
        number += 1
    else:
        number += 1
'''
#模範回答
num = 0
while num<=50:
    print(num)
    num+=2
#模範回答の癖に10からって条件を無視しててなんかムッっとなりました。




#１）0~9の値をfor文を使用してを一つずつ表示。ただし7になったらループを終了させよ
for num in range(10):
    if num == 8:
        break
    print(num)


#２）0~9の値を一つずつ表示せよ。ただし4の場合は表示しない。(continueを使用)
for num in range(10):
    if num == 4:
        continue
    else:
        print(str(num) + ":練習問題2ですよー")

#３）passを使って0~9の値を一つずつ表示せよ。ただし4の場合は表示しない(passを使用)
num = 0
for num in range(10):
    if num == 4:
        pass
    else:
        print(str(num) + ":練習問題3ですよー")


#模範解答 あれ全部条件だったんだ・・・まぁあんまり気にしなくてもいいんじゃないかな。
#1)
for i in range(9):
    if i==7:
        break

#2)
for i in range(9):
    if i==4:
        continue

#3)
for i in range(9):
    if i==4:
        pass
    else:
        print(i)