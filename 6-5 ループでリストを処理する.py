# Your code here!

# ループでリストを処理する
team = [
    "勇者",
    "戦士",
    "魔法使い"
]
print(team)
print(team[0])


for person in team:
    print(person)
#このfor in の処理は昨日やった問題で使ったよね。

for person in team:
    print(person + "が、スライムと戦った")

#enumrate変数君
for (i, person) in enumerate(team):
    print(str(i + 1) + "番目の" + person + "が、スライムと戦った")
# この変数君は
# for (index_number, list_element) in enumrate(list_name)
# ってな感じで動作する変数。

numbers = [1,2,3,4,5]
results = []
for item in numbers:
    results.append(item * 10)

print(results)

#appendで代数演算子使えたんだ、って感じです。


List = ["知らない事は",2,"多いと",4,"河川から望む学区外",]
for (j, number) in enumerate(List):
    print(number)
    print(":" + str(j) + ":")

'''以下、出力結果
知らない事は
:0:
2
:1:
多いと
:2:
4
:3:
河川から望む学区外
:4:
こういう動きしてまっせーっていう確認でございます
amazarashiさんの「月曜日」って曲の歌詞を拝借しております。
'''