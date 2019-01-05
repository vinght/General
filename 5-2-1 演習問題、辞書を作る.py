#演習課題
'''
「指定の文字を辞書にしてみよう」
skillsという辞書に、下記の要素をキーと値を組にして保存して、print関数で出力してください

職業 : "戦士"
体力 : 100
魔法力 : 200
ゴールド : 380

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
{'職業': '戦士', '魔法力': 200, '体力': 100, 'ゴールド': 380}
'''

skills = {
    "職業":"戦士",
    "体力":100,
    "魔法力":200,
    "ゴールド":380
}

print(skills)
# ちょっとびっくらポンした事
# データの値はstring typeじゃないとダメなのかと思ってたけど
# int typeでも平気だった。辞書って自由 


#演習問題 2
'''
「ハッシュの中身を出力してみよう」
右のコードには、skillsという辞書が定義されています。
この辞書をprint関数を使って出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
{'魔法力': 200, '体力': 100, '職業': '戦士', 'ゴールド': 380}
'''
# 辞書の中身を出力してみよう

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# この下で、辞書を出力してみよう
print(skills)


# バカにされてる気分です。


# 演習問題 3
'''
「辞書の特定の値を出力してみよう」
右のコードには、辞書が定義されています。
この辞書から、「職業」というキーに対応する値をprintで出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
戦士
'''
# 辞書の特定の値を出力してみよう

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# この下で、辞書から出力してみよう
print(skills["職業"])

#出力の仕方は大体リストと一緒。
# 作り方だけ少し違うんだなーって事だけ意識すればいいかなーと言う印象です。 