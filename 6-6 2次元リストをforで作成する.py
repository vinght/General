# Your code here!

# 2次元リストをforで作成する
# 今まではリストを直接定義してきた
# for を使えば処理の繰り返しを使ってリストの初期値を指定することも出来るらしい

numbers = [
    1,
    2,
    3,
]#←いままでのリスト

new_numbars = [1 for i in range(10)]
print(new_numbars)
print(len(new_numbars))
'''出力結果
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
10
処理としては
何某 for 変数 in range(回数)
の何某をrange(回数)分、出力するよ！って文っぽい

'''
new_numbars = [i * 2 for i in range(10)]
print(new_numbars)
print(len(new_numbars))
'''出力結果
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
10
恐らく処理としては変数i に最初何も入って無くて0が出力
次に i にrengeの 1 が引数になって、
その引数(1) * 2 = 2
んでこっからが何か特殊でそのまま 2 3 ...と引数として入るのかと思ったら
4, 6, ...と普通に掛け算が始まってるので
恐らく
変数 * n for 変数 in range(回数)
って文は変数が 0 の時だけ処理が違うっぽい。
'''

#forを使ってリストを作れることを利用して二次元リストを作成してみようのコーナー
numbers2 = [[1 for i in range(3)] for j in range(4)]
print(numbers2)
'''出力結果
[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
要は
何某 for 変数 in range(回数)
の 何某 の部分がリストを作るfor文になったってだけ。
'''

numbers2 = [[1 for i in range(3)] for j in range(4)]
print(numbers2)
numbers2[0][1] = "in_the_end"
print(numbers2)

'''
[[1, 1, 'in_the_end'], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
要素の更新は別にしなくても・・・'''

# 大きなリストを作りたい時はfor inを使うと便利だそうだよ
# 覚えておいて損はないけどどういう時に使うのかの理解度がほんわかほわほわだから不安だよ！