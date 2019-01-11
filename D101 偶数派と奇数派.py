# https://paiza.jp/works/challenges/258/retry

inp = input().split()

if int(inp[0]) % 2 == 0 and int(inp[1]) % 2 == 0:
    print("No")
elif int(inp[0]) % 2 == 1 and int(inp[1]) % 2 == 1:
    print("No")
elif int(inp[0]) == 1 and int(inp[1]) == 1:
    print("No")
elif int(inp[0]) % 2 == 0 or int(inp[0]) % 2 == 1 or int(inp[0]) == 1:
    print("yes")
elif int(inp[1]) % 2 == 0 or int(inp[1]) % 2 == 1 or int(inp[1]) == 1:
    print("Yes")