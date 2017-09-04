def find_longest(word_list):
	word_len = []
	for n in word_list:
		word_len.append((len(n),n))
	word_len.sort()
	return word_len[-1][1]
print(find_longest(["chandu","raghav","excercises","ghostreturn"]))
