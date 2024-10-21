
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)
    cd = character_count(text)
    sort_dic(cd)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    counter = text.split()
    count = 0
    for word in counter:
        count += 1
    return count

def character_count(text):
    book_string = text.split()
    letter_count = {}
    for word in book_string:
        for character in word:   
            char = character.lower()
            if char not in letter_count:
                letter_count[char]  = 1
            if char in letter_count:
                letter_count[char] += 1
    return letter_count

def sort_func(cd):
    return cd[""]

def sort_dic(cd):
    sorted = cd.sort(reverse = True, key=sort_func)
    print(sorted)
    


main()  