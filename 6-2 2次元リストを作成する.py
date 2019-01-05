# Your code here!

# 2次元リストを作成する

player = "盗賊"

team_a = [
    "勇者",
    "戦士",
    "魔法使い",
    player,
]
#普通のリスト

print(team_a)
print(team_a[0])

team_b = [
    team_a[0],
    team_a[1],
    team_a[2],
]
print(team_b)
print(team_b[0])

#リストの要素をリストで指定したらこうなりましたって話。



team_c = [
    "勇者",
    "戦士",
    "魔法使い",
]

team_d = [
    "盗賊",
    "忍者",
    "商人",
]

team_e = [
    "スライム",
    "ドラゴン",
    "魔王",
]

teams = [
    team_c,
    team_d,
    team_e,
]
print(teams)
'''
[['勇者', '戦士', '魔法使い'], ['盗賊', '忍者', '商人'], ['スライム', 'ドラゴン', '魔王']]
'''
#こんな感じでpythonのリストは他のリストを丸ごと入れられるらしいよ。うわばみかな？

print(teams[0][0])

# んでこれが二次元リストの出力法。
# 要はteamsの中のindex number 0 の
# team_cを参照して
# その中のindex number 0 に振り分けられてる
# 勇者
# が出力されましたって事です

print(teams[1][1]) #忍者を出力
print(teams[2][0]) #スライムを出力

# 二次元リスト
# 要約するとリストにinされたリスト
# しかもそのリストの中にまたリスト作れるから実際は
# 多次元リストって呼ばれてます。
# 終わり