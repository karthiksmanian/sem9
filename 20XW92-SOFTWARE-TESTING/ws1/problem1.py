tcfile = open('testcases.txt', 'r')
ansfile = open('answers.txt', 'r')

lines = tcfile.read().splitlines()
tcs = len(lines)
tc_list = list()

for i in range(tcs):
	testcase = list()
	for c in lines[i].split(','):
		testcase.append(int(c))

	tc_list.append(testcase)

lines = ansfile.read().splitlines()
ans_len = len(lines)
ans_list = list()

for i in range(ans_len):
	ans_list.append(int(lines[i]))

def get_min(arr):
	if not arr:
		return None

	minval = 1e9

	for elt in arr:
		minval = min(minval, elt)

	return minval
i = 1
for tc, ans in zip(tc_list, ans_list):
	computedval = get_min(tc)
	if not computedval:
		print(f"tc{i} Empty List as input\n")

	print(f"Min value of tc{i} is {computedval}")

	if computedval==ans:
		print(f"Actual ans is {ans}")
		print("Passed.")
	else:
		print(f"Actual ans is {ans}")
		print("Failed.")
	i += 1
