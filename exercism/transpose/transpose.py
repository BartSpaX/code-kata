from itertools import zip_longest

def transpose(lines):
    lines = zip_longest(*lines.splitlines(), fillvalue='*')
    return '\n'.join(''.join(row).rstrip('*').replace('*', ' ') for row in lines)