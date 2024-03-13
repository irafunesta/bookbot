
def main():
    path = "books/frankenstein.txt"
    book_content = read_book(path)
    num_of_words = book_content.split()
    letter_count = number_of_letters(book_content)

    print(f"------------- Report of {path} -------------")

    print(f"\ttotal words: {len(num_of_words)}")

    allchar = dictionary_to_list(letter_count)
    allchar.sort(reverse=True, key=sort_on)

    for ele in allchar:
        print(f"\tLetter {ele["char"]} is used {ele["freq"]} times.")
    
    print(f"------------ End of Report {path} ---------")

    
def read_book(path):
    with open(path) as f:
        return f.read()

def number_of_letters(text):
    letter_set = {}
    for c in text:
        key = c.lower()
        if key in letter_set:
            letter_set[key] += 1
            continue
        letter_set[key] = 1
    return letter_set

def dictionary_to_list(dictionary):
    list = []
    for key in dictionary.keys():
        if key.isalpha():
            list.append({"char":key, "freq":dictionary[key]})
    return list

def sort_on(dict):
    return dict["freq"]
main()