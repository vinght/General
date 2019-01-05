# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王

line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")



# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王
import random
line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")

# ランダムな数を作る範囲を調べる
num = len(line)
print("敵は" + str(num) + "匹")

# ランダムな数を生成
attack = random.randrange(num)

#選んだ敵に、「会心の一撃！」と表示
print(line[attack] + "に会心の一撃！" + line[attack] + "を倒した！")


#random.randrange とは？ 
# randomモジュールの一つだよ！いちいち書くのが面倒だから以下参照だよ
'''
range(start, stop, step) 
の要素からランダムに選ばれた要素を返します。
この関数は
choice(range(start, stop, step))
と等価ですが、実際には range オブジェクトを生成しません。

位置引数のパターンは range() のそれと一致します。
キーワード引数は、この関数に望まれない方法で使われるかもしれないので
使うべきではありません。
'''