import datetime

today = datetime.date.today()#今日の日付
toDay_nowtime = datetime.datetime.today()#時間まで 変数に代入することで効力を発揮してくれる

datetime.date.today().year
datetime.date.today().day

datetime.datetime # 日時（日付と時刻）
datetime.date # 日付
datetime.time # 時刻
datetime.timedelta # 時間差・経過時間


print(today)
print(toDay_nowtime) #これだと.以下の時間まで表示される、ので指定したものだけを表示させたい時は
print(toDay_nowtime.strftime('%y/%/%A/%H/%M'))


'''
%d : 0埋めした10進数で表記した月中の日にち
%m : 0埋めした10進数で表記した月
%y : 0埋めした10進数で表記した西暦の下2桁
%Y : 0埋めした10進数で表記した西暦4桁
%H : 0埋めした10進数で表記した時 （24時間表記）
%I : 0埋めした10進数で表記した時 （12時間表記）
%M : 0埋めした10進数で表記した分
%S : 0埋めした10進数で表記した秒
%f : 0埋めした10進数で表記したマイクロ秒（6桁）
%A : ロケールの曜日名
%a : ロケールの曜日名（短縮形）
%B : ロケールの月名
%b : ロケールの月名（短縮形）
%j : 0埋めした10進数で表記した年中の日にち（正月が'001'）
%U : 0埋めした10進数で表記した年中の週番号 （週の始まりは日曜日）
%W : 0埋めした10進数で表記した年中の週番号 （週の始まりは月曜日）%d : 0埋めした10進数で表記した月中の日にち
%m : 0埋めした10進数で表記した月
%y : 0埋めした10進数で表記した西暦の下2桁
%Y : 0埋めした10進数で表記した西暦4桁
%H : 0埋めした10進数で表記した時 （24時間表記）
%I : 0埋めした10進数で表記した時 （12時間表記）
%M : 0埋めした10進数で表記した分
%S : 0埋めした10進数で表記した秒
%f : 0埋めした10進数で表記したマイクロ秒（6桁）
%A : ロケールの曜日名
%a : ロケールの曜日名（短縮形）
%B : ロケールの月名
%b : ロケールの月名（短縮形）
%j : 0埋めした10進数で表記した年中の日にち（正月が'001'）
%U : 0埋めした10進数で表記した年中の週番号 （週の始まりは日曜日）
%W : 0埋めした10進数で表記した年中の週番号 （週の始まりは月曜日）
'''