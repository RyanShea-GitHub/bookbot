
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count(text)
    character_count(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    counter = text.split()
    count = 0
    for word in counter:
        count += 1
    print(f"Total number of words is: {count}")
    return count

def character_count(text):
    counter = text.split()
    letter_count = {}
    for character in counter:
        for letter in character:
            char = letter.lower()
            if char not in letter_count:
                letter_count[char]  = 1
            if char in letter_count:
                letter_count[char] += 1
    print(letter_count)
    return letter_count


main()
        