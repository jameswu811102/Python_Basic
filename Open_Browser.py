# 檔案需拖曳到cmd中執行

import os
import sys

if len(sys.argv) < 2:
	print("請輸入網址!")
else:
	url = sys.argv[1]
	os.system("start {}".format(url))

