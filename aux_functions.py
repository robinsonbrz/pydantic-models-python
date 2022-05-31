def list_titles(data) -> None:
    print("Titles: ________________")
    for num, book in enumerate(data):
        print(f"Title {num}: {book['title']}")
    print()

def list_keys_values(data) -> None:
    print("Key value: ________________")
    for num, book in enumerate(data):
        print(f"Title {num}")
        for key, value in book.items():
            print(f'{key}:   {value}')
        print()
