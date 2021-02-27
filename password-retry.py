password = "a123456"
i = 3
while i > 0:
	pwd = input("パスワードを入力してください：")
	if pwd == password:
		print("ログイン成功")
		break
	else:
		i = i - 1
		print("パスワード間違いました、あと", i,"回")

