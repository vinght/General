# ループでリストを操作する

team = ["勇者", "戦士", "魔法使い"]
print(team)
print(team[0])
team.append("盗賊")

for i in range(5):
    print(i)



print(team)


for i in team:
    print(i)
'''
出力結果
['勇者', '戦士', '魔法使い']
勇者
0
1
2
3
4
['勇者', '戦士', '魔法使い', '盗賊']
勇者
戦士
魔法使い
盗賊
'''