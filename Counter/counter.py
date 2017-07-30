from collections import Counter

	text="the vauof dft the works"\
	"fdkfdi the workd"


word = text.split()
print(word)
counter =Counter(word)
print(counter)
final=counter.most_common(2)
print(final)