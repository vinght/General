# https://paiza.jp/challenges/36/show

times = int(input())
hello = "Hello "
for i in range(times):
    words = input()
    if i + 1 == times:
        hello = hello + words + (".")
    else:
        hello = hello + words + (",")
print(hello)