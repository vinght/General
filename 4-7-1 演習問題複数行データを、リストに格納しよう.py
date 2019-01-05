# 演習課題
'''
「標準入力から読み込んだ複数行を出力しよう」
右のコードエリアのプログラムは、RPGの敵の名前を、入力エリアから複数行データとして読み込んで出力します。
この文字列を、「＊＊が現れた」という形式で出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです

入力される値
スライム
モンスター
ゾンビ
ドラゴン
魔王

標準入力からの値取得方法はこちらをご確認ください

期待する出力値
スライムが現れた
モンスターが現れた
ゾンビが現れた
ドラゴンが現れた
魔王が現れた

元
# 読み込んだ複数行を出力する

import sys
for line in sys.stdin.readlines():
	msg = line.rstrip()
	print(msg)
'''

# 読み込んだ複数行を出力する

import sys
for line in sys.stdin.readlines():
	msg = line.rstrip()
	print(msg + 'が現れた')



#演習課題2
'''
「読み込んだ複数行のカンマ区切りデータを出力しよう」
右のコードエリアのプログラムは、入力エリアから複数行データを読み込みます。
入力エリアには、RPGの敵の名前と匹数が、カンマ区切りで用意してあります。
読み込んだデータをカンマで分割して、「AがB匹現れた」と出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

入力される値
スライム,30
モンスター,23
ゾンビ,15
ドラゴン,3
魔王,1

標準入力からの値取得方法はこちらをご確認ください

期待する出力値
スライムが30匹現れた
モンスターが23匹現れた
ゾンビが15匹現れた
ドラゴンが3匹現れた
魔王が1匹現れた


import sys
for lines in sys.stdin.readlines():
    enemy = lines.rstrip().split(',')
    print(str(enemy)+ 'が'  '匹現れた')


line = input()
test = line.split(",")
print(test)

import sys
for lines in sys.stdin.readlines():
    enemy = lines.rstrip().split(',')
    if enemy == str:
    print(enemy)
'''
import sys
for line in sys.stdin.readlines():
	# ここに、文字列を分割して、出力するコードを書く
	enemy = line.rstrip()
	print(enemy)

'''
import sys
for line in sys.stdin.readlines():
	line = line.split()
	print(line)

出力値
['スライム,30']
['モンスター,23']
['ゾンビ,15']
['ドラゴン,3']
['魔王,1']
'''



import sys
for line in sys.stdin.readlines():
	enemy = line.sprit()
	print(enemy)


# 以下正解
import sys
for lines in sys.stdin.readlines():
	enemys = lines.rstrip().split(",")
	print(enemys[0] + "が" + enemys[1] + "匹現れた")

#リストが複数、生成されてたから全部別扱いなのかと思ったら
# index number 
# が全部一緒だった
# そんなん聞いてねーし。