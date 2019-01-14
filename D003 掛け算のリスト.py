# https://paiza.jp/challenges/34/show

number = input()

for i in range(1,10):
    if i == 9:
        cal = int(number) * i
        print(cal)
    else:
        cal = int(number) * i
        print(cal, end=" ")