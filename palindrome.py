#######################
# palindrome
#######################


def pal():
	textInput = input("Please enter a string for the palindrome test: ")
#	text = textInput
	text = textInput[::-1]
	if textInput == text:
		print("success: the word is a palindrome")
	print(text)
	return text

pal()
