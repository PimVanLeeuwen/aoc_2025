from utils import *

class ID:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b

def solve(input_data: str):
    id_objects = [ID(id_str.split('-')[0], id_str.split('-')[1]) for id_str in read_lines(input_data)[0].split(',')]
    parts = [0,0]

    for id_obj in id_objects:
        for i in range(int(id_obj.a), int(id_obj.b) + 1):
            str_i = str(i) # string of the ID
            n = len(str_i) # length of the ID string

            # Part 1 check: check if the ID can be split into two equal halves
            if n % 2 == 0 and str_i[:n//2] == str_i[n//2:]:
                parts[0] += int(str_i)

            # Part 2 check: check if the ID can be constructed by repeating a smaller substring
            for j in range(1, n//2 + 1):
                if n % j == 0:
                    if str_i == str_i[:j] * (n // j): # check if the string is equal to the substring repeated
                        parts[1] += i
                        break # no need to check larger substrings

    return parts