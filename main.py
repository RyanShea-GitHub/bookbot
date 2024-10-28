
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)
    cd = character_count(text)
    sf = organize_dic(cd)
    print_report(book_path, wc, cd, sf)
    


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

def sort_func(sf):
    return sf["Number"]

def organize_dic(cd):
    sorted = []
    for set in cd:
        sorted.append({"Letter": set, "Number": cd[set]})
    sorted.sort(reverse=True, key=sort_func)
    return sorted    

def print_report(book_path, wc, cd, sf):
    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} wrods found in the document.\n")
    for set in sf:
        if set["Letter"].isalpha():
            print(f"the '{set['Letter']}' character was found {set['Number']} times.")


main()  