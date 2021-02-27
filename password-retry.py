password = "a123456"
i = 3
while i > 0:
	i = i - 1
	pwd = input("パスワードを入力してください：")
	if pwd == password:
		print("ログイン成功")
		break
	else:
		print("パスワード間違いました！")
		if i > 0:
			print("あと", i, "回です")
		else:
			print("パスワード間違いました、アカウントロックしました。")

