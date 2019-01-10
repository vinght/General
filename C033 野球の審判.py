#https://paiza.jp/challenges/139/show

input_lines = input()

strike = []
ball = []

for i in range(int(input_lines)):
    inp = input()
    if inp == "strike":
        strike.append(inp)
        if len(strike) == 3:
            print("out!")
            break
        print("strike!")
    elif inp == "ball":
        ball.append(inp)
        if len(ball) == 4:
            print("fourball!")
            break
        print("ball!")