from colorama import init, Back, Style
import time
import os

init()

# 秒數操控
remain = 1

# 紅綠燈循環迴圈
while True:

	# 將秒數固定在0~9秒，使號誌得以循環
	remain = remain % 10

	# 用秒數來判斷應顯示之號誌顏色
	if 1 <= remain <= 5:
		print(Back.RED, Style.NORMAL, Back.RESET, Style.RESET_ALL)
		print(remain)
		time.sleep(1)

	elif remain == 6:
		print(" ", Back.YELLOW, Style.NORMAL, Back.RESET, Style.RESET_ALL)
		print(remain)
		time.sleep(1)

	elif remain == 0 or remain >= 7:
		print("   ", Back.GREEN, Style.NORMAL, Back.RESET, Style.RESET_ALL)
		print(remain)
		time.sleep(1)

	# 秒數會持續 +1
	remain += 1

	# 刷新每秒的顯示
	os.system("cls")
