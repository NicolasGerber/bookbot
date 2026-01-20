import string
def find_words(path):
    with open(path) as f:
        text = f.read()
    num_words = 0
    for word in text.split():
        num_words +=1
    return print(f'Found {num_words} total words')

def count_chars(path):
    with open(path) as f:
        text = f.read()
    keys = string.ascii_lowercase + string.digits + string.punctuation
    keyboard_dict = {char: 0 for char in keys}

    for letter in text.lower():
        for char in keyboard_dict:
            if char == " ":
                continue
            if letter == char:
                keyboard_dict[char] +=1
    data_list = []
    for key in keyboard_dict:
        value = keyboard_dict[key]
        data_list.append([key,value])
    lenght = len(data_list)
    for i in range(lenght):
        for j in range(0, lenght - i - 1):
            current_item = data_list[j]
            next_item = data_list[j + 1]

            current_count = current_item[1]
            next_count = next_item[1]

            if current_count < next_count:
                data_list[j] = next_item
                data_list[j + 1] = current_item
    for item in data_list:
        char = item[0]
        count = item[1]
        if count > 0:
            print(f"{char}: {count}")

    return keyboard_dict
