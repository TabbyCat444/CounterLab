user_text = input("Please enter a single character to count followed by a space and then a word or phrase to count the"
                  " character in: ")

print("Your character is present this many times: ", + user_text[1:].count(user_text[0:1]))
