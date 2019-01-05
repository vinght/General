# Your code here!

# リストのおさらい
enemyArray = ['スライム','モンスター','ドラゴン']
print(enemyArray)
print(enemyArray[0])
number = len(enemyArray)
print(number)


# 辞書の具体例
enemyDictionary ={
    "ザコ":"スライム",
    "中ボス":"ドラゴン",
    "ラスボス":"魔王",
}
# 辞書の基本的な要素の追加の仕方は
# "kye":"データの値",
#  末尾の,は区切りだよ。
#  って書くよ
# 因みに
# データの値は intger typeでも大丈夫だよ。辞書って結構自由なんだ。

# んで辞書の値を取り出したい場合はkyeを指定するよ。さっき例えたけど
# 付箋名だね
# 出力の仕方は
# 辞書名[key name] 
# で出力出来るよ。因みにリストと同じように 
# 大括弧内にkey nameを書いて指定しないとエラーが出るから注意ね。
# string typeのみ、シングル or ダブルクオーテーションで指定しないとエラー吐くからね

print(enemyDictionary)
print(enemyDictionary["ザコ"])
print(enemyDictionary["中ボス"])
#出力結果は
# {'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
# スライム
# ドラゴン
# key名、データの値名、両方確認出来るね。
# key名からデータの値も呼び出せたよ。





# keyを変数で指定する
level = "ザコ"
print(enemyDictionary[level])
'''出力結果
スライム'''


level = "ラスボス"
print(enemyDictionary[level])
'''出力結果
魔王'''

# と辞書のkeyは変数で指定することも出来る、何でもアリだなぁ
# 
# # まぁあったり前田のクラッカーだが辞書に存在しないkeyを指定するとエラーが出るよ
# エラー名は 
# keyError "kye name"
# ってエラーを吐き出すよ
# エラーが出なかったら出なかったで驚きだが。