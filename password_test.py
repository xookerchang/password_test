# 密碼retry function
# password = 'a123456'
# 讓使用者重複輸入三次密碼
# 最多輸入三次
# 如果正確 印出 “登入成功”！
# 如果不正確 印出 “密碼錯誤” ＿還有幾次機會


password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！')
		break # get out the loop
	else:
		i = i-1
		print('請重新輸入密碼, 還剩下', i ,'次機會')
		if i == 0:
			break
		
