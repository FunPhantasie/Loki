alphabet="abcdefghijklmnopqrstuvxyz"
alphabet_c = "qporetzuilkhjgfndmsaybxcvw"

alphabet_c_upper=alphabet_c.upper()
get_letter= 0
keyword =  []

text = "Hallo mein Name"

key = 0
if 0 <= key <= 26:
	for letter in text:
		if letter== " ":
			keyword.append(letter)
			continue
		get_letter = (alphabet.index(letter.lower()) + key)%27 #Mit leerzeichen
		print(str(get_letter)+" " ,end="")
		if letter.isupper():
			keyword.append(alphabet_c_upper[get_letter])
		else:
			keyword.append(alphabet_c[get_letter])
	print("")
	print("".join(keyword))
else:
	print("Key must be between 1 and 26!")
