# https://paiza.jp/challenges/91/show

times = int(input())

variable1 = 0
variable2 = 0
n = 0

for i in range(times):
    test = input().split()
    if test[0] == "SET" and int(test[1]) == 1:
        variable1 = int(test[2])
    elif test[0] == "SET" and int(test[1]) == 2:
        variable2 = int(test[2])
    elif test[0] == "ADD":
        variable2 = variable1 + int(test[1])
    elif test[0] == "SUB":
        variable2 = variable1 - int(test[1])
    test = []
print(str(variable1) + " " + str(variable2))