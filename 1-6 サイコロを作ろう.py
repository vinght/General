# coding: utf-8
#数の表示とサイコロ
'''
変数が数値の場合は""←が要らん、まぁ文字として認識させる訳じゃないから当然だが
number = 100
print("スライムが" + number + "匹あらわれた")
#これを実行するとエラーが出る、原因は数値と文字を混ぜて連結してるためだからだよ
'''

#そこでこうやって
number = 100
print("スライムが" + str(number) + "匹あらわれた")
'''
str関数と呼ばれる物を使い
number(数値データ)を文字データに変換して入れてやると
str関数はPCの中で数値として扱われてるデータを文字データに変換する関数だよ
strは英語で文字列を表すstringの略だよ！覚えておこう！
じゃあこの100と言う数値をランダムで表示させるために
random関数 randint関数
と呼ばれるものを使ってみよう'''

#↓random関数
'''
import random まずは
import random
のコードを書いて
number = random.random() #さっき100だった個所を「rondom.rondom()」と入力
print("スライムが" + str(number) + "匹あらわれた")
これを走らせると全ての文字がランダムに表示されるから
数字の範囲を指定してみる'''

import random #importと言うのは組み込むという意味 日本語訳するとランダムを組み込みますよって意味な
    #import無かったら機械からしたらは？何？ってなるから注意な！
number = random.randint(1,100)
'''
さっき.rondomだった部分を「rondint(数字,数字)」と入力する
このカッコ内の数字は「引数」と呼ばれてて、引数が複数ある場合は,(カンマ)で区切る'''

print("スライムが" + str(number) + "匹あらわれた")

import random
number = random.randint(1,20)
print("スライムが" + str(number) + "匹あらわれた")
#   さっきの場合だと引数の範囲は1～100に指定されてるから引数の範囲を絞ると







#！カンマの部分をドットにする事多いから注意して

#関数とは
'''Pythonが持つ特別な機能を呼び出す方法です。
print関数のように標準で利用できる関数と、モジュールを組み込み(インポート)してから利用する関数があります。

関数の例：
print(data)	：指定したデータを出力する
str(number)	：数値を、数を表す文字に変換する

モジュールを組み込んでから利用する関数は、モジュール名と関数名を「.」(ピリオド)でつないで記述します。

モジュールで組み込む関数の例：
random.random()	：0から1までのランダムな数値を出力する
random.randint(a, b)	：aからbまでの間のランダムな整数を出力する'''


#引数とは
'''関数の引数(ひきすう)とは、関数に与えるデータです。
引数は、関数に続くカッコの中に記述します。引数が複数ある場合は、「,」(コンマ)で区切ります。

引数の例：
print(data)のdata	：出力するデータをdataで指定する
str(number)のnumber	：数から文字に変換するデータをnumberで指定する
'''


#戻り値とは
'''
関数の戻り値(もどりち)とは、関数の処理結果のデータです。返り値と呼ぶ場合もあります。

random.randint(0, 10)という関数を呼び出すと、0から10までのランダムな数が戻り値となります'''


#変にインデントを使うとプログラムが走らなくなる、これはおそらくif文のようなある条件を指定するためにインデントを使ってねと言う意図があるためだと思われる
#インデント、危険！