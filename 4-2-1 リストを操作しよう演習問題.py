'''
演習課題「リストに要素を追加してみよう」
右のコードエリアには、4つの要素を持つweaponリストが定義されています。
このリストの末尾に、「石斧」という要素をappend関数で出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
['木の棒', '鉄の棒', '鉄の剣', '銅の剣', '石斧']
'''
# リストに要素を追加する

weapons = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を追加するコードを記述する
weapons.append("石斧")

print(weapons)

'''
演習課題 2
「リストの要素を上書きしてみよう」
右のコードエリアには、4つの要素を持つweaponリストが定義されています。
このリストの3番の要素を、「石斧」に書き換えてください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
['木の棒', '鉄の棒', '鉄の剣', '石斧']




# リストの要素を上書きする

weapon = ["木の棒", "鉄の棒", "鉄の剣", "サビた剣"]
# ここに、要素を上書きするコードを記述する


print(weapon)
'''

# リストの要素を上書きする

weapons = ["木の棒", "鉄の棒", "鉄の剣", "サビた剣"]
# ここに、要素を上書きするコードを記述する
weapons[3] = ("石斧")

print(weapons)

'''
演習課題3
「リストから要素を削除してみよう」
右のコードエリアには、4つの要素を持つweaponリストが定義されています。
このリストから、2番の要素を削除してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
['木の棒', '鉄の棒', '銅の剣']

# リストの要素を削除する

weapon = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を削除するコードを記述する


print(weapon)

一回目の回答
# リストの要素を削除する

weapons = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を削除するコードを記述する
weapons.pop[3]  ←ここが違った、[] ではなく()でindex numberを指定する事

print(weapons)'''

# リストの要素を削除する

weapons = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を削除するコードを記述する
weapons.pop(2)

print(weapons)