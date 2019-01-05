# coding: utf-8 #←これはエンコードルール(coding:)って言ってコメントとかに日本語を使えるようにするためのもの
# データの種類
number = 100 		#数値
strings = "paiza"	#文字列
print(number)
print(strings)
'''
上記のプログラムを実行すると数値と文字列がそれぞれprintされる
なんでこんな書き方の違いがあるかって？
それはプログラミングでは数値と文字列といったデータの種類を厳密に区別してるからだよ
このようなデータの種類を「データ型」と呼ぶ
'''


number = 100 + 30		#数値
strings = "ハロー" + "paiza"	#実は文字同士を連結するときも+(プラス)が使える
print(number)
print(strings)

number = "100" + "30"		#ダブルクオーテーションつけると数字じゃなくて文字扱いになる
strings = "ハロー" + "paiza"	#実は文字同士を連結するときも+(プラス)が使える
print(number)
print(strings)


number = 100 + 30		#数値
strings = "ハロー" + "paiza"
print(number)
print(strings)
print(str(number) + strings)

'''str関数は数値データを文字データに置き換えるコマンドだから
プログラムがちゃんと実行される、プログラム実行の際はデータの型が一致してるか
考えよう！'''

print(number + 20)


'''
    じゃあ例えばintから文字へのデータ型変換はstr()で出来るのはご周知の通りだが
    数値→文字にデータ型を変換したい場合はどうするかと言うと
    int()で変換するといい例えば
'''
import random
test = "5"
print(int(test) + 7)
