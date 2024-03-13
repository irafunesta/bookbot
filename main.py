
def read_book(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    print(file_contents)


def main():
    read_book("books/frankenstein.txt")

main()