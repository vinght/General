# リストの要素を取り出す

team = ["勇者", "魔法使い"]
print(team)
print(team[0])
print(team[1])

num = 0
print(team[num + 1])

'''
print(team[10])
これ試しに書いてるだけだけど
pythonではリストの範囲外にアクセスしようとすると
エラーを吐き出すよ。あったり前な気がするけどね！
他の言語ではどうなるんだろうね！

だからlistの長さを確認するコードがあるよ！'''

print(len(team))

'''
ぶっちゃけこれ復習だよね！
len
とは
length
の略で長さって意味だよ！
発音がダルいからわざわざ書かなくても覚えてるね！
'''
#こっからちょっと実験

team.append("戦士")

print(team)
print(len(team))

#やっぱり処理順で要素が更新されてた。