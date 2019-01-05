'''for文
今回も、1から100までの数字を出力してみます。
やや複雑になってきますが、書き方がわからなくなってしまった場合にはスライドで復習してみましょう。'''
'''
for number in range(1,101):
    number <= 100
    print(number)'''



# for文を完成させてください
for number in range(1,11):
    number += 1
    number %= 3
    if number == 0:
        print(number)
    # print('3の倍数です')



for number in range(1,11):
    print(number)
    if number % 3 == 0:
        print(f'{number}は3の倍数です')

for number in range(1,11):
    if number % 3 == 0:
        print(f'{number}は3の倍数です') # ここのfは改行して表示させるよってコマンドな！
    else:
        print(number)


# for文を完成させてください
for number in range(1,11):
    if number % 3 == 0:
        print(f'{number}は3の倍数です')
    else:
        print(f'{number}は3の倍数ではない')
    
    
# if文を用いて、numberが3の倍数の時に「3の倍数です」、そうでないときは数字を出力してください

# if文を用いて、numberが3の倍数の時に「3の倍数です」、そうでないときは数字を出力してください


'''
+a            # 正数
-a            # 負数
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算
a % b         # a を b で割った余り
a ** b        # a の b 乗
a // b        # 切り捨て除算


ビット演算子(~, &, |, ^, <<, >>)
下記のビット演算子が定義されています。
~a            # ビット反転
a & b         # AND:論理積(aもbも1のビットが1)
a | b         # OR:論理和(aまたはbが1のビットが1)
a ^ b         # XOR:排他的論理和(aまたはbが1のビットが1)
a << b        # b ビット左シフト
a >> b        # b ビット右シフト



代入演算子(=, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, <<=, >>=)
下記の代入演算子が定義されています。++ や -- はサポートされていないので
代わりに a += 1 や a -= 1 を用います。
a = b         # a に b を代入する
a += b        # a = a + b に同じ
a -= b        # a = a - b に同じ
a *= b        # a = a * b に同じ
a /= b        # a = a / b に同じ
a %= b        # a = a % b に同じ
a **= b       # a = a ** b に同じ
a //= b       # a = a // b に同じ
a &= b        # a = a & b に同じ
a |= b        # a = a | b に同じ
a ^= b        # a = a ^ b に同じ
a <<= b       # a = a << b に同じ
a >>= b       # a = a >> b に同じ



比較演算子(==, !=, <, >, <=, >=, <=>, ===)
下記の比較演算子が定義されています。
a == b           # a が b と等しい
a != b           # a が b と異なる
a < b            # a が b よりも小さい
a > b            # a が b よりも大きい
a <= b           # a が b 以下である
a >= b           # a が b 以上である
a <> b           # a が b と異なる
a is b           # a が b と等しい
a is not b       # a が b と異なる
a in b           # a が b に含まれる
a not in b       # a が b に含まれない
'''