# https://paiza.jp/challenges/239/show

inp = input().split()

inp.sort()
cal = int(inp[3])*10 + int(inp[1])
cal1 = int(inp[2])*10 + int(inp[0])
answer = cal + cal1
print(answer)
