# 年齢入力のプルダウン作成

'''
for age in (1,101)
print('<select name=\'age\'>')
print('<option> + str(age) + </option>')
print('</select>')
'''# bad！処理の順序を考えてなーい



print('<select name=\'age\'>')
for age in (1,101):
    print('<option>' + str(age) + '</option>')
print('</select>')