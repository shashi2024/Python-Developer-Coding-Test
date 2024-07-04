def count_words_in_file(filename: str) -> int:
    with open(filename, 'r') as file:
        content = file.read()
    return len(content.split())


print(count_words_in_file("example.txt"))
