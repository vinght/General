# Your code here!



def say_hello():
    print("hello world")

say_hello()

#関数の中では数値を計算することも出来る

# 引数と戻り値を追加する
def sum(x):
    print(x + 20)
sum(3)
# sum(3)がxにポーイって渡されて、で
# x +20のxの中にポーイって渡された値を使って計算が出来るって訳。
# この引数を複数設定する事だって出来るんやで。 

def sum1(x, y):
    print(str(x + y) + ":サム１やでー")

sum1(300 , 200)

#引数が複数ある場合も定義するのが楽だよねと言う例です。



def sum2(x, y):
    return x + y

num1 = sum2(3, 2)
print(str(num1) + ":サム２やでー")
num2 = sum2(300, 400)
print(str(num2) + ":サム２のナム２やでー" )


#これで関数定義に戻り値が追加された。
# こんな感じで引数と戻り値を使って関数を定義すれば
# 処理を一か所にまとめる事ができちゃうんだ、便利だね。


#inputされた文字型がintなら動かす、strならダメだよってプログラムを組みたい。
inp1 = input()
inp2 = input()
def calculate():
    if type(inp1) is str or type(inp2) is str:
        print("数字を入力してやー")
    else:
        print(str(int(inp1) + int(inp2)) + ":インプットした値やでー")
        pass


calculate()
