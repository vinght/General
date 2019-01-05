# coding: utf-8
# if文による条件分岐　elif文
import random
number = random.randint(1,3)
if number == 1:
	print( "スキ！")	#条件式が成立したときの処理
elif number == 2:
    print('どちらでもない')# 条件式2が成立したときの結果
else:
	print( "キライ")	#条件式が成立しなかったときの処理
print(number)

'''
条件式が実行される順番は上から下へと順に処理される
重要なのはインデント、実行順、そしてそれ以外はelseで締める
この場合ifが実行されたとしたらそれ以降のelif,elseはスキップされる
だから例えば条件式2に条件式3の内容を持ってくると見づらい
!!ちなみにelifとelse後に無理にコメントアウトとかしてコメントつけるとバグるよ
'''