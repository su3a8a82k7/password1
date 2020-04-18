password = 'a123456'
 
t = 3 #剩餘次數
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
			print('登入成功')
			break #脫出迴圈
		#elif pwd != password:
		#t = t - 1
		#print('密碼錯誤, 還有', t,'次機會')
		#if t == 0
		#break #脫出迴圈
	else:
		t = t - 1
		print('密碼錯誤, 還有', t,'次機會')
		if t == 0:
			print('鎖住')
			break #脫出迴圈