import re

def is_paired(input_string):
    brackets, has_pair = re.sub(r"[^{}[\]()]", "", input_string), 1
    while has_pair:
        brackets, has_pair = re.subn(r"{}|\[]|\(\)", "", brackets)
    return not brackets