def multiply_by2(item):
    return item * 2

new_list = list(map(multiply_by2, [1, 2, 3]))

print(new_list)


def convert_to_capitals(characters):

    characters = str(characters)

    return characters.upper()


char_list = list(map(convert_to_capitals, ["andreas", "sotiris", "chris", "tasos"]))

print(char_list)