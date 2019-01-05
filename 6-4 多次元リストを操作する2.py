# Your code here!

# 2次元リストの基本操作

teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(teams)


teams.append(["メタルモンスター","シルバーモンスター","ブラックモンスター",])
print(teams)
print(len(teams))
# appendは要素を追加するメソッドだったよね、
# まぁ書かなくてもいいけどリストも追加出来るよ
# 多次元リストではリストは一つの「要素」としてとらえられてる
# って考えたら色々楽なんじゃないのかな。 

teams[0].append("レッドドラゴン")
print(teams)
print(len(teams))
print(len(teams[0]))

#リスト内のリスト、もうわけわからんから二次元リストって呼称するけど
# 二次元リストに要素を追加したい場合は上記の様に、二次元リストを
# 指定して(teams[0].append)から
# 要素を入れればいいんじゃよ 



del teams[1]
print(teams)
print(len(teams))

del teams[0][2]
print(teams)
print(len(teams[0]))

#リストを要素としてみたら以下略


# 与太話
# insert
# で要素を追加できるらしいのだが、リストの中にリスト入れれるかな
# と思って以下のコードを実行した所 
teams.insert(1,["旧市街地","市街地","郊外区"])
print(teams)
print(teams[0])
print(teams[1])


'''出力結果
[['勇者', '戦士'], ['旧市街地', '市街地', '郊外区'], ['スライム', 'ドラゴン', '魔王'], ['魔
法使い'], ['メタルモンスター', 'シルバーモンスター', 'ブラックモンスター']]
['勇者', '戦士']
['旧市街地', '市街地', '郊外区']
と
'''
# リストが入るんじゃなくて押しのけて
# index number 1 
# に新リストが割り込んだ形になりました
# 入らないかー・・・と思った次第でございます
# 因みにinsert([1],["旧市街地","市街地","郊外区"])
# って書いたらエラー吐かれました。 