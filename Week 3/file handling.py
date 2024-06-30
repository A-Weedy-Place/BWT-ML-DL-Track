def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print("File Stuff:\n", data)
            return data
    except FileNotFoundError:
        print(f"The file '{file_path}' doesnt exist.")
    except IOError:
        print(f"An error occurred while reading: '{file_path}'.")


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            word_count = len(data.split())
            print(f"The file '{file_path}' contains {word_count} words.")
            return word_count
    except FileNotFoundError:
        print(f"The file '{file_path}' doesnt exist.")
    except IOError:
        print(f"An error occurred while reading: '{file_path}'.")


def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to the file '{file_path}'.")
    except IOError:
        print(f"An error occurred while writing: '{file_path}'.")


if __name__ == "__main__":
    # Reading and printing the contents
    file_data = read_file('uwu.txt')

    # Counting the number of words
    if file_data:
        count_words('uwu.txt')

    # Writing user input
    user_input = input("Enter some text to write to 'uwu.txt': ")
    write_file('uwu.txt', user_input)
