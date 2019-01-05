'''
pytonだと


例

colors =['blue', 'pink']


colors[0] = 'red' これが使えるのは[]リストだけ
()タップルでは使えませーん

for name in colors:
    print(name)

動作としては一時的に、for文内だけでcolorsの要素、この場合
'blue', 'pink'
の各要素を
name
に代入している。だからfor文 内でのprint(name)はリストの要素が出力されんだよ、覚えとけ


print(name)←これは使えない
if,for,while文で作った変数はその中でしか使えないため
上記の出力は出来ないという理解でよい


'''

for i in range(10):
    print(i) # i変数とは恐らくIndex_variableのI

'''
for i in range()
i は範囲 つまりfor i の数だけ繰り返す
range(始まり,終わり)
までを繰り返す
って処理

？rangeとは？
たとえばint typeのrenge object(数列を生成する物)を作りたい時0～xと指定したくなるよね
そういう時に使えるのが
range(int)
どういう動作なのかと言うとさっき
range(10)
って書いたよね？それを書いたら0～9まで数列を生成される
プログラムだと数列的に考えるからすべての始まりが
0 になる、神様みたいだね

例えば
1～10までの数列を指定したい時とかは
range(1,11)
と指定しなければならない

何故ならば、処理的には
0,1,2,3,4,5,6,7,8,9,10(11個やで)

と11個の数列が出来上がってて
そっから0を排除したいから

range(1,11)と始まりを    1を指定しないといけないわけなんだ
なーんか面倒くさいよね！

'''



#以下 paizza式for文


# for inによるループ処理
'''
for couter_variable(カウンタ変数) in loop_range(繰り返す範囲):←コロン必須
    繰り返し処理(この部分がループ動作の内容になる) ←インデントを忘れずに

'''

for i in range(6,11):
    print('hello world:' + str(i)) 




# https://www.javadrive.jp/python/for/index3.html
