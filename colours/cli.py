

def main():
    """CLI endpoint for running `colours` command.

    A neat command for printing a coloured ANSI colour code reference to the terminal.

    Args:
        None

    Returns:
        None
    """

    # basic colour sequences
    for i in range(30,38):
        print(f'\033[{i}m', f'\\033[{i}m', f'\033[0m', end='')
        print('\t', end='')
        print(f'\033[{i+60}m', f'\\033[{i+60}m', f'\033[0m')

    other_codes_of_note = {
        'reset': 0,
        'bold': 1,
        'italic': 3,
        'underlined': 4,
        'invert': 7,
        'crossed': 9,
    }

    # go up 8 lines
    print('\033[8A', end='')
    for k,v in other_codes_of_note.items():
        # go to end of line
        print('\033[24C', end='')
        print('\t', end='')
        print(f'\033[{v}m', f'{k} -', f'\\033[{v}m', '\033[0m')

    # (r,g,b) colour sequences
    print('\033[38;2;255;188;217m','(r,g,b) - \\033[38;2;r;g;bm', '\033[0m')
    print('\033[48;2;66;158;157m','(r,g,b) - \\033[48;2;r;g;bm', '\033[0m')

    # cursor movement sequences
    # go up 2 lines, to end of line
    print('\033[2A', '\033[28C', end='')
    print('\t', end='')
    print('move by x -', '\\033[xA')
    print('\033[28C', '\t', end='')
    print('(ABCD -> up/down/right/left)')

if __name__ == "__main__":
    main()
