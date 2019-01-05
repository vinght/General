'''
演習課題「文字列をカンマで分割してみよう」
右のコードエリアには、RPGのプレイヤーが、team_strという文字列に、カンマで区切られて代入されています。
この文字列を、split関数を使ってカンマのところで分割してください。
そして、結果をリストに格納して、print関数で出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
['勇者', '戦士', '忍者', '魔法使い']

'''

#文字列をカンマで分割する

team_str = "勇者,戦士,忍者,魔法使い"
list = team_str.split(',')
print(list)

'''
演習課題2
「英文の単語数を数えよう」
右のコードエリアには、ある英文がstrという文字列に代入されています。
この文字列を、split関数を使って、スペースのところで分割して、単語の数を出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！
'''
#英文の単語数を数える

str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"
list = str.split()
print(len(list))

'''
演習課題「標準入力から読み込んだURLを分割しよう」
右のコードエリアのプログラムは、入力エリアのURLを読み込みます。
読み込んだURLを「/」で分割して、リストとしてprint関数で出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

入力される値
https://paiza.jp/cgc/users/ready

標準入力からの値取得方法はこちらをご確認ください

期待する出力値
['https:', '', 'paiza.jp', 'cgc', 'users', 'ready']
'''
# 標準入力から読み込んだURLを分割する
# https://paiza.jp/cgc/users/ready


url_str = input().rstrip().split("/")
print(url_str)