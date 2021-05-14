#######################
# wordCount
#######################


def words():
	textInput = input("Please enter a sentence for wordCount test: ")
	newInput = textInput.split(" ")
	print("There are", len(newInput), "words in that sentence")
	return newInput

words()
