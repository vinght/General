# 演習課題「同じテキストを指定回数出力する」
# 標準入力とループ処理
line = int(input()) #ここのデータをint_typeにする意識が無かった。
for i in range(line):
    print('スライムがあらわれた')



# 演習課題「標準入力とfor文の組み合せ」
'''
標準入力で2つ（２行）の整数が与えられます。
1つ目の数値から２つ目の数値までを、1ずつ増加させながら、1行ずつ順番に出力するプログラムを作成してください。

たとえば、3と5という数値が与えられた場合、次のように出力します。

```
3
4
5
```

※1行目の数値は、２行目の数値よりも必ず小さい値が与えられるものとします。

プログラムを実行して、正しく出力されれば演習課題クリアです！



入力される値
5
12
_____________________

期待する出力値
5
6
7
8
9
10
11
12

'''
# 回答１
line = input().rstrip()
for i in range(7):
    i = line + 1
    print = (i)
line = input().rstrip()


# 回答2
# 標準入力とループ処理
line = input('2').rstrip()
for i in range(5,12):
    line = i + 1
    print(i)
line = input('2.5').rstrip()
print(line)


# 回答3 そもそも意図してる回答と違うっぽい
line = input().rstrip()
for i in range(5,12):
    line = i + 1
    print(i)
line = input().rstrip()
print(line)


# 正解
num1 = int(input()) #入力1、つまり5
num2 = int(input()) #入力2、つまり12

for i in range(num1, num2 + 1): #範囲は5～11+1=12
    print(i) #で出力すれば勝手にループ処理してくれるからおしまい。僕の人生もおしまい

'''
for i in range(7):
    i = i + 1
print(i)
'''
