from collections import OrderedDict
import random

## Read file
input_path = raw_input("Enter filename of input (ASCII): ")
try:
	input_file = open(input_path, "r")
except IOError:
	print "Could not open file"
	exit()
input_txt = input_file.read() #Read everything into RAM. For big texts this might not be advisable but it works for now
input_file.close()


text = input_txt.split()


word_list = {} #Format: {"word" : ["follower1", "follower2"], "anotherword" : } etc.
num_words = len(text)

for idx, word in enumerate(text):
	if word not in word_list.keys():
		word_list[word] = [] #assign an empty list of followers for now
		if idx < num_words:
			try: #Using Try / Catch to avoid an IndexError when trying to do idx + 1 on the last element
				next_word = text[idx + 1]
				word_list[word].append(next_word)	
			except IndexError: 
				pass
	else:
		if idx < num_words:
			try:
				next_word = text[idx + 1]
				word_list[word].append(next_word)
			except IndexError:
				pass
			

#Now we've built the word list, generate some text

current_word = "the" #Word we want to start with.
output = []
length = 1000 #output length in words
for i in range(1, length):
	output.append(current_word)
	if len(word_list[current_word]) > 0:
		next_word = random.choice(word_list[current_word])
		current_word = next_word
	else:
		current_word = random.choice(text)
	
print ' '.join(output)







