# 取り込んだデータをリストに格納する
'''
・入力
スライム,モンスター,ドラゴン,魔王
'''


line = input().rstrip().split(",")
# split関数は引数で指定した記号でデータを分割して
# リストで取得する関数になる
# ここの場合は 
# ① input関数で読み込んだデータを
# ② rstrip関数 で受け取り、行末の改行を削除して
# ③ split関数で受け取り、引数で指定した「,」で受け取って
# (別に,区切りじゃなくて でもいいよ)
# ⑤ 最後に list として代入している


print(line)
print(len(line))

for enemy in line:
    print(enemy + "があらわれた！")



'''
・出力
['スライム', 'モンスター', 'ドラゴン', '魔王']
4
スライムがあらわれた！
モンスターがあらわれた！
ドラゴンがあらわれた！
魔王があらわれた！
'''

# そもそもsplit関数って何ぞや？
# 例えば test = ("あ" "い" "う" "え" "お")
# って関数を作ったとしよう
# これlist化したいなぁって思ったときに使うのが
# split関数
# 
# paiza曰く
# split関数	与えられたデータを指定の記号で分割し、リストとして戻す
# と言ってるので解釈は大体あってるはず