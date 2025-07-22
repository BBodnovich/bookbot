import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def get_num_words(file_contents):
    words_list = file_contents.split()
    return len(words_list)


def get_char_counts(file_contents):
    output_dict = {}
    for letter in file_contents.lower():
        if letter not in output_dict:
            output_dict[letter] = 1
        elif letter in output_dict:
            output_dict[letter] += 1
    return output_dict


def sort_on(items):
    return items["num"]


def sort_char_counts(letter_counts):
    output_list = []
    for key, value in letter_counts.items():
        output_list.append({"char": key, "num": value})
    output_list.sort(reverse=True, key=sort_on)
    return output_list


def main():
    # Validate input path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(sys.argv[1])

    # Read contents of the file
    book_text = get_book_text(book_path)

    # Count the words and letters in the file contents
    word_count = get_num_words(book_text)
    letter_count = get_char_counts(book_text)

    # Sort the letter_count dictionary
    sorted_letter_count = sort_char_counts(letter_count)

    # Print the output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_letter_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
