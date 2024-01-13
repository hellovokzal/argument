def text(text, arg):
	num = -1
	num1 = len(arg)
	while True:
		num = num + 1
		num1 = num1 + 1
		if text[num:num1] == arg:
			return text[num:num1]
