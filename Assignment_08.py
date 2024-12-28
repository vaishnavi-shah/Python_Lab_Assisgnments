# 1. Write a Python program to count the occurrences of each word in a given sentence.
string = "To change the overall look of your document. To change the look available in the gallery"
words = string.split()
word_count = {}
for word in words:
    word = word.strip(".").lower()  # Remove punctuation and convert to lowercase
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:", word_count)
#==================================================================

# 2. Write a Python program to remove a newline in Python.
string = "\nBest \nDeeptech \nPython \nTraining\n"
modified_string = string.replace("\n", "")
print("String after removing newlines:", modified_string)
#==================================================================

# 3. Write a Python program to reverse words in a string.
string = "Deeptech Python Training"
reversed_string = " ".join(string.split()[::-1])
print("Reversed words in the string:", reversed_string)
#==================================================================

# 4. Write a Python program to count and display the vowels of a given text.
string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = {v: string.count(v) for v in vowels if v in string}
print("Vowels and their counts:", vowel_count)

