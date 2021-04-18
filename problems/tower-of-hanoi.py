TOWERS = {'A': ['6','5','4','3','2','1'], 'B': [], 'C': []}

def other(tower1, tower2):
	together = tower1 + tower2;
	if together == 'AB' or together == 'BA':
		return 'C'
	elif together == 'BC' or together == 'CB':
		return 'A'
	else:
		return 'B'

def move(n, start, end):
	if n == 1:
		TOWERS[end].append(TOWERS[start].pop())
	else:
		between = other(start, end)
		move(n - 1, start, between)
		move(1, start, end)
		move(n - 1, between, end)

def print_towers():
	a_len = len(TOWERS['A'])
	b_len = len(TOWERS['B'])
	c_len = len(TOWERS['C'])
	longest_tower = max(a_len, b_len, c_len)

	for i in range(longest_tower - 1, -1, -1):
		a_value = TOWERS['A'][i] if i < a_len else ''
		b_value = TOWERS['B'][i] if i < b_len else ''
		c_value = TOWERS['C'][i] if i < c_len else ''
		print(a_value + '\t' + b_value + '\t' + c_value)
	print("A\tB\tC")


print("------BEFORE------")
print_towers()
print("------------------\n")

move(6, 'A', 'C');
print("------AFTER-------")
print_towers()
print("------------------")


