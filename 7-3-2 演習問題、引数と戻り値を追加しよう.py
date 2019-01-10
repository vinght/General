#演習課題
'''
「掛け算関数を呼び出してみよう」
右のコードには、2つの引数を掛け算するmultiply関数が定義されています。
この関数を呼び出して、「3ｘ4」の計算結果を表示してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
12
'''


# 掛け算関数を呼び出してみよう

def multiply(x, y):
    return x * y

# この下に関数呼び出しを記述する
print(multiply(3, 4))



#演習課題 2
'''
「掛け算関数を作成してみよう」
右のコードには、multiply関数を呼び出していますが、関数の処理が記述してありません。
xとyの二つの引数を掛け算した結果を返すよう、関数にコードを追加してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
12
35
408
'''

# 掛け算関数を作成してみよう

def multiply1(x, y):
    # この下に処理を記述する
    return x * y

print(multiply1(3, 4))
print(multiply1(5, 7))
print(multiply1(12, 34))





#演習課題 3
'''
「九九の表を作成してみよう」
右のコードは、九九の2の段を出力するプログラムです。
このプログラムを修正して、九九を1の段から9の段まで出力してください。
各段は、行末で改行してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
1, 2, 3, 4, 5, 6, 7, 8, 9
2, 4, 6, 8, 10, 12, 14, 16, 18
3, 6, 9, 12, 15, 18, 21, 24, 27
4, 8, 12, 16, 20, 24, 28, 32, 36
5, 10, 15, 20, 25, 30, 35, 40, 45
6, 12, 18, 24, 30, 36, 42, 48, 54
7, 14, 21, 28, 35, 42, 49, 56, 63
8, 16, 24, 32, 40, 48, 56, 64, 72
9, 18, 27, 36, 45, 54, 63, 72, 81
'''

# 九九の表を作成してみよう

# 九九の表を作成してみよう

def multiply2(x, y):
    return x * y

for num in range(1,10):
    print(multiply2(1, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1, 10):
    print(multiply2(2, num), end="")
    if num < 9:
        print(", ", end="")
print()


for num in range(1,10):
    print(multiply2(3, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(4, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(5, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(6, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(7, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(8, num), end="")
    if num < 9:
        print(", ", end="")
print()

for num in range(1,10):
    print(multiply2(9, num), end="")
    if num < 9:
        print(", ", end="")
print()

#あまりにも長すぎる…

for number in range(1, 10):
    for num in range(1, 10):
        print(multiply2(number, num), end="")
        if num < 9:
            print(", ", end="")
    print("")

#これで解決ですね。