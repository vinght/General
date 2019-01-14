# https://paiza.jp/challenges/266/show


time_and = input().split()
student = []
for i in range(int(time_and[0])):
    student = input().split()
    record = int(student[0]) - int(student[1])*5
    if record >= int(time_and[1]):
        print(i + 1)
    elif int(time_and[1]) == 0:
        if int(-record) == int(-record):
            print(i + 1)
    elif int(-record) >= 0:
        pass
    else:
        pass