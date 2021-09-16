import os
import codecs

command = ""

# 初始工作路徑
cwd_path = os.getcwd()

while command != "0":
	os.system("cls")

	# 列出所在路徑的檔案(1)
	if command == "1":
		index = 0
		for file in os.listdir(cwd_path):
			if os.path.isfile(cwd_path + "/" + file):
				print(index, file)
				index += 1

		print("")

	# 列出所在路徑的資料夾(2)
	elif command == "2":
		index = 0
		for folder in os.listdir(cwd_path):
			if os.path.isdir(cwd_path + "/" + folder):
				print(index, folder)
				index += 1

		print("")

	# 顯示檔案內容(3)
	elif command == "3":
		index = 0
		file_dict = {}
		for file in os.listdir(cwd_path):
			if os.path.isfile(cwd_path + "/" + file):
				print(index, file)
				file_dict[index] = file
				index += 1

		print("")

		open_index = input("請輸入讀取檔案索引：")
		try:
			with codecs.open(cwd_path + "/" + file_dict[int(open_index)], "r", "utf-8") as f:
				os.system("cls")
				print(f.read())
				print("")
		except UnicodeDecodeError:
			with codecs.open(cwd_path + "/" + file_dict[int(open_index)], "rb") as f:
				os.system("cls")
				print(f.read())
				print("")
		except (KeyError, ValueError):
			pass
			os.system("cls")
			print("無該檔案")
			print("")

	# 刪除檔案(4)
	elif command == "4":
		index = 0
		file_dict = {}
		for file in os.listdir(cwd_path):
			if os.path.isfile(cwd_path + "/" + file):
				print(index, file)
				file_dict[index] = file
				index += 1

		print("")

		del_index = input("請輸入刪除檔案索引：")
		try:
			os.remove(cwd_path + "/" + file_dict[int(del_index)])
			os.system("cls")
		except (KeyError, ValueError):
			pass
			os.system("cls")
			print("無該檔案")
			print("")

	# 執行檔案(5)
	elif command == "5":
		index = 0
		file_dict = {}
		for file in os.listdir(cwd_path):
			if os.path.isfile(cwd_path + "/" + file):
				print(index, file)
				file_dict[index] = file
				index += 1

		print("")

		execute_index = input("請輸入執行檔案索引: ")
		try:
			os.startfile("{}".format(cwd_path + "/" + file_dict[int(execute_index)]))
			os.system("cls")
		except (KeyError, ValueError):
			pass
			os.system("cls")
			print("無該檔案")
			print("")

	# 進入資料夾(6)
	elif command == "6":
		index = 0
		dir_dict = {}
		for folder in os.listdir(cwd_path):
			if os.path.isdir(cwd_path + "/" + folder):
				print(index, folder)
				dir_dict[index] = folder
				index += 1

		print("")

		enter_index = input("請輸入進入資料夾索引: ")
		try:
			cwd_path = os.getcwd() + "/" + dir_dict[int(enter_index)]
			os.system("cls")
		except (KeyError, ValueError):
			pass
			os.system("cls")
			print("無該資料夾")
			print("")

	# 刪除資料夾(7)
	elif command == "7":
		index = 0
		dir_dict = {}
		for folder in os.listdir(cwd_path):
			if os.path.isdir(cwd_path + "/" + folder):
				print(index, folder)
				dir_dict[index] = folder
				index += 1

		print("")

		del_index = input("請輸入刪除資料夾索引：")
		try:
			os.rmdir(cwd_path + "/" + dir_dict[int(del_index)])
			os.system("cls")
		# 資料夾內部有其他文件
		except OSError:
			for file in os.listdir(cwd_path + "/" + dir_dict[int(del_index)]):
				os.remove(cwd_path + "/" + dir_dict[int(del_index)] + "/" + file)
			os.rmdir(cwd_path + "/" + dir_dict[int(del_index)])
			os.system("cls")
		except (KeyError, ValueError):
			pass
			os.system("cls")
			print("無該資料夾")
			print("")

	# 回上層資料夾(8)
	elif command == "8":
		cwd_path = os.path.split(cwd_path)[0]

		os.system("cls")

	# 轉至當前工作路徑
	os.chdir(cwd_path)
	# 顯示工作路徑
	print("工作路徑:", cwd_path)
	# 指令提示
	print(
		"        (0) 離開程式\n        (1) 列出檔案\n        (2) 列出資料夾\n        (3) 顯示檔案內容\n        (4) 刪除檔案\n        (5) 執行檔案\n        (6) 進入資料夾\n        (7) 刪除資料夾\n        (8) 回上層資料夾\n")
	# 顯示指令輸入列
	command = input("操作：")
