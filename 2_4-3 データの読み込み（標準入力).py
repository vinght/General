# inputによる入力処理
'''
標準入力
もともとはLINUXなどのUnix系OSで用意されていた仕組みです。
標準入力に対応するようにプログラムを作っておけば
プログラム実行時に、ファイルを読み込んだり、
キーボードからデータを読み込んだり
パラメータを指定したりというように
入力先を切り替えることができます。
入力って言うのは人から機械へ語り掛ける認識でいいと思われ
プログラム言語にはこのようなデータを読み込むための命令が用意されてる
それが
標準入力ってのなんだ
標準入力ってのはファイル、キーボード、実行時に指定
など人からプログラムへデータを読み込ませることが出来る
'''



line = input('文字を入力してください')
print('hello')
#'' or "" 内の入力されるときに出力される文字、つまり入力するときに出て来る待機メッセージみたいなもんなんだ。何書いてもいいよ




# 標準入力の注意点、標準入力ではデフォルトでstring typeとして入力を受け付けるからinteger typeにしたかったら宣言しなきゃならんのよ
line = int(input('数字を入力してください')) #こっちはint型の入力、int型の入力したかったらこういう形にしないといけないよ
print(line * 10)







# 演習課題「標準入力からテキストを取得する」 入力はハローワールド
line = input()
print(line)
# 期待される出力はハローワールド、だからこれで正解


# 演習課題「標準入力から数値を取得して計算する」 入力は1234
line = int(input())
print(line * 100)

# 期待される出力は123400 ゆえに正解