# 九九乘法表
"""
想法:
1x1 1x2 1x3 1x4 1x5...
2x1 2x2 2x3 2x4 2x5...
3x1 3x2 3x3 3x4 3x5...

觀察後由兩個數字組成，且兩個數字的範圍都是1~9
"""

# 土法煉鋼
n1 = list(range(1, 10))
n2 = list(range(1, 10))

for i in n1:
	for j in n2:
		result = "{}x{}={}".format(i, j, i*j)
		if j < len(n2):
			print("{:<8}".format(result), end=" ")
		else:
			print("{:<8}".format(result), end="\n")

print("#"*50)

# 快速
for i in range(1, 10):
	for j in range(1, 10):
		result = "{}x{}={}".format(i, j ,i*j)
		if j < len(range(1, 10)):
			print("{:<8}".format(result), end=" ")
		else:
			print("{:<7}".format(result), end="\n")


