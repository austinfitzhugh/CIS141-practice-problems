#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
#it. Write a Python program that:
#- Reads the file
#- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#- Counts how many times each word appears
#- Creates a dictionary of the words and their counts
#- Print the dictionary to the console

with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()
    
print("Enter 5 words to count in the lyrics: ")
words = []

for i in range(5):
    word = input(f"Word {i + 1}: ").lower()
    words.append(word)

word_counts = {}
for word in words:
    count = lyrics.split().count(word)
    word_counts[word] = count

print("\nWord Frequencies:")
print(word_counts)
