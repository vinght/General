# 複数行データをリストに格納する


'''
import sys
for line in sys.stdin.readline(): #readline(s)複数形になってない
    print(lipane.rstrip())'''

import sys
for line in sys.stdin.readlines():# この場合はreadlins関数で複数行のデータを読み取って
    print(line)



# そして出力が終わった場合にループ処理を終わらせるってコード
# 文字列の冒頭の空白文字だけを取り除くlstripメソッド
# 同じく末尾の空白文字だけを取り除くrstripメソッド






'''
「sys」
Python のインタプリタや実行環境に関連した変数や
関数がまとめられたライブラリです。
じゃあそもそも
import sys
とは何ぞや？
import
は組み込むって意味だというのは先日習ったが
その後に random だったり sys だったり書いてるよね
これってなぁに？と言われると
import sys
を書いたらsys.何某っていうモジュール？が使えるようになりますよ的な
解釈でなんとなく合ってる。今回の場合は
sys.stdin
は(input() の呼び出しも含む) すべての対話型入力に使われます。
'''
# tips
# 対話型入力とは
# コンピューターが、ディスプレイなどを通じてユーザーにデータの入力などを要求し
# それに応じて処理を行っていくという
# あたかも対話をしながら仕事を進めていくように見える処理方式。
# 会話型処理とも呼ぶ 


# readline() は入力した行を縦に表示する関数。
# 1行毎に読み込み、その処理を繰り返す

# readlines() は一度に全ての行を標準入力から読み込む関数。
# ファイルを全て読み込み、1行毎に処理を行う




# 複数行データを、リストに格納しよう

import sys
arrays = []
for line in sys.stdin.readlines():
    arrays.append(line.rstrip())
print(arrays)

# 因みにこのコード、paizaでしか使えないからな。
# 本当にこのままでいいのかわからなくなってきた。 