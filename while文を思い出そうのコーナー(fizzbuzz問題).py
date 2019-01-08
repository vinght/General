count = 0
while(count < 101):
    if count % 15 == 0:
        print(str(count) + ':fizzbuzz')
    elif count % 3 == 0:
        print(str(count) + ':fizz')
    elif count % 5 == 0:
        print(str(count) + ':buzz')
    else:
        print(count)
    count += 1


# 以上、fizzbuzz問題でした。
# 分かった事、while,if,elif,elseの復習になりました。
# インデントがどのように処理されて、どのように動くか再認識しました。
# 前にやった事ある気がします 