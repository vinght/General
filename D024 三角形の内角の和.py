

'''
期待する出力
平面上の三角形の 2 つの角の角度 a, b が改行区切りで与えられるので残りの 1 つの角度を出力して下さい。

最後は改行し、余計な文字、空行を含んではいけません。
条件
すべてのテストケースで以下の条件を満たします。

・1 ≦ a ≦ 179
・1 ≦ b ≦ 179
・2 ≦ a + b ≦ 179

a, b は正の整数
入力例1
60
90
出力例1
30
入力例2
45
45
出力例2
90
'''

input_lines = int(input())
input_lines2 = int(input())
angle = 180 - input_lines + input_lines2 # これだと何故か出力が210になった、ってか計算の順番を考えたら当たり前に210になる。
print("angle") #しかもここstring typeだし・・・

#以下正解
input_lines = int(input())
input_lines2 = int(input())
angle = 180 - (input_lines + input_lines2) #括弧で優しく包んでみたら期待した出力値になった
print(angle)