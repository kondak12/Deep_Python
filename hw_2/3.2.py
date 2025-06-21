# Task 3.2 -------------------------------------------------------------------------------------------------------------
def unic_string_count_generator(string: str, len_split: int):
    while len_split != len(string):
        end_index = 0
        while len_split != end_index:
            end_index += 1
            yield string[:end_index:]
        string = string[1:len(string)]