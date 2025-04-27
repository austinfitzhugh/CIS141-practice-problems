#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("please enter a sentence: ")
word = input("please enter a word to find: ")
words_found = word in sentence
print(words_found)
