team = ["勇者", "戦士", "魔法使い"]
#print(team)
#print(team[0])
team.append("盗賊")

print("<select name ='job'>")
for job in team:
    print("<option>" + job + "</option>")
print("</select>")

#このコードはhtmlのコードだがプルダウンリスト
# と呼ばれる何かクリックして選ばせる方式のリストを作るためのコードですん
# 多分色々とお世話になるのでなんとなーく覚えておこう