def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = count_letters(text)
    print(f"{num_words} words found in the document")
    for letter, count in letters.items():
        print(f"{letter}: {count}")
    #sort letter and put in dictionary
    sorted_letters_dict = dict(sorted_letters(letters))
    for letter, count in sorted_letters_dict.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
        else:
            print(f"The '{letter}' character was found {count} times")
            
        



def get_num_words(text):
    words = text.split()
    return len(words)

def sorted_letters(letters):
    isalpha = lambda x: x.isalpha()
    return sorted(letters.items(), key=lambda x: x[1], reverse=True)


def get_book_text(path):
    with open(path) as f:
        return f.read()

#count each how many times each letter is used using a dictionary
def count_letters(text):
    letters = {}
    parse_text = text.lower()
    for letter in parse_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()
