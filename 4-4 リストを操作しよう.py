# リストの要素を操作する

team = ["勇者", "魔法使い"]
print(team)
print(team[0])

team.append("戦士")
#team[3] = "遊び人" こんな感じで要素のない場所に追加は出来ないよ。
# append使えって事ですね！
print(team)

team[2] = ("ドラゴン")
#だけど要素の上書きは出来るよ。ってか前にやったね
#因みに今は追加された要素をさらに上書きしてるよ
#要素さんはよく変わるよ！キューティーハニーみたいだね！
print(team)

team.pop(0)
#list_name.popで特定のelementを削除出来るよ
#pop関数って言うらしいよ

print(team)

("'ω'")