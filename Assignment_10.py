# 1. Write a function in Python to read the content from a text file "ABC.txt" line by line and display the same on screen.
def read_file():
    with open("ABC.txt", "r") as file:
        for line in file:
            print(line.strip())

#==================================================================

# 2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”.
def count_words():
    with open("ABC.txt", "r") as file:
        word_count = sum(len(line.split()) for line in file)
    print(f"Total number of words: {word_count}")

#==================================================================

# 3. Write a function in Python to count uppercase characters in a text file “ABC.txt”.
def count_uppercase():
    uppercase_count = 0
    with open("ABC.txt", "r") as file:
        for line in file:
            uppercase_count += sum(1 for char in line if char.isupper())
    print(f"Total uppercase characters: {uppercase_count}")

#==================================================================

# 4. Write a function display_words() in Python to read lines from a text file "story.txt" 
#    and display those words, which are less than 4 characters.
def display_words():
    with open("story.txt", "r") as file:
        for line in file:
            words = line.split()
            short_words = [word for word in words if len(word) < 4]
            print(" ".join(short_words))

#==================================================================
