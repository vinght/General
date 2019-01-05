#演習課題
'''
「画像を順番に出力する」
右側のエディターエリアのプログラムを元に、items_imgリストをitems_orderリストの順に、
1行づつHTMLで画像を表示してみましょう。

HTMLで画像を1行ずつ表示する場合は以下のようにimgタグを利用します。
<img src=URL><br>

期待する出力値
http://paiza.jp/learning/images/sword.png
http://paiza.jp/learning/images/shield.png
http://paiza.jp/learning/images/potion.png
http://paiza.jp/learning/images/crystal.png
'''

# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_orders = [
    "剣",
    "盾",
    "回復薬",
    "クリスタル"
    ]

# ここから下を記述しよう
for items_name in items_orders:
    print("<img src='" + items_imges[items_name] + "'>")
    print("<br>")




#演習課題 2
'''
「アイテムリストを作ってみよう」
右側のエディターエリアのプログラムを元に、アイテムリストを作ってみましょう。
標準入力で出力するアイテム数と複数行のアイテム名の入力があります。
それを元に、items_imgで定義された画像を改行せず順番に出力してみましょう。
画像の出力にはimgタグを使い、src属性に画像のファイル名を指定します。

※標準入力で与えられるアイテム名は、items_imgに無いアイテムは
出てこないものとします。

入力される値
6
回復薬
盾
クリスタル
クリスタル
剣
剣

標準入力からの値取得方法はこちらをご確認ください

期待する出力値
'''
# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

'''分からなかったので回答を見ました
# ここから下を記述しよう
line = input() #6 int type
line2 = input() #回復薬 key
line3 = input() #盾 kye 
line4 = input() #クリスタル
line5 = input() #クリスタル
line6 = input() #剣
line7 = input() #剣

print("<img src='" + item_images[line] + "'>")'''

#以下回答
# 画像用ハッシュ
items_img = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# 出力するアイテム数を変数に代入
item_cnt = int(input())

# 標準入力にあるアイテムを出力する
while item_cnt > 0:
    item = input()
    print("<img src = '" + items_img[item] + "'>")
    item_cnt = item_cnt - 1

# 今回の反省点、while文で回すべきだった。
# for文に執着しすぎた。頭が固かったね。

# んで、最初のitem_cntで入力された6を利用して
# 6が0になるまで処理を繰り返すって条件を作る
# 次に画像データを表示させるプログラム

# item = input()
# print("<img src = '" + itemes_img[item] + "'>")

# を書きます、そして次に条件を満たさせるためのコード
# item_cnt = item_cnt - 1

# と書きます

# while文の存在は頭の片隅にはあったけど、意図に沿わなかったら
# どうしようとか考えてた、軟弱物！プログラムは自由ぞ！ 