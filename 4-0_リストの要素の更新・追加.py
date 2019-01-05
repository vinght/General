'''
リストの要素の更新・追加
リストの要素を
更新しよう！
んじゃあリストの内容を変えたいけど


リストの要素を更新してみましょう。
リスト[インデックス番号] = 値
とすることで
リストの指定したインデックス番号の要素を更新することができるよ！

例えば
wokers = [
    'ヴぃんと',
    'さくら君',
    'Himo君',
    'エピソードニキ',
]
wokers = ['ヴぃんと','さくら君','Himo君',]

たとえばさくらニキがお風呂行ってエピソードニキが来ました！
さくらニキの要素をエピソードニキに変えたい！
って時に

！ wokers[1] = ('エピソードニキ') ←間違い
wokers[1] = 'エピソードニキ' 
↑ 正しくは()要らない。だって最初からstring typeだから

list名[index number] = (element)
でelementが追加されるわけさ


ってして「さくら君」を「エピソードニキ」に更新したわけさ。ざまぁみろ(悪意はないよ！)

リストの要素の更新・追加、リストに要素を追加しよう。

リストには、新しく要素を追加することもできます。 
「リスト.append(値)」とすることで、すでに定義されているリストの末尾に新たな要素を追加することができるよ！
因みに
append
は
[動][多動] (…に)添える、付加する
って意味だよ！リストに値を付加するって意味になるね！意味が機能してるよ！

後々、プログラム上で後からリストに要素を追加したかったら使うコマンド
それが.appendだよ。
予想だけれどこの.appendは大体inputとセットになると思うよ！多分ね！


じゃあさくらニキが風呂から帰ってきました！
そしたらさくらニキを追加しないとだね！
wokers.append('さくらニキ')
で
wokers('ヴぃんと','エピソードニキ','Himoニキ','さくらニキ',)
とさくらニキの要素が追加されたよ！
追加された要素はどんどん増えていくからね！気を付けてね！
因みに、.appendはプログラム上で行う処理だから
listに直接要素を加えるのとは意味合いが違うよ！
最初listに直接要素加えればいいじゃんとか思ってたけどそんなん幻想だよ
'''
# 具体的なPG上での要素の追加ァッ
character = input('職業を入力してください')
teams = [
    "勇者ァ",
    "魔法使い",
    "賢者",
]
teams.append(character)


print(len(teams))
print(teams)