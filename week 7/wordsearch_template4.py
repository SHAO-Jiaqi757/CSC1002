
MIN_LEN = 4
g_puzzle = []
g_puzzle_t = []
g_dictword = []
g_dir = ['n','e','s','w']
g_incr = {
      'n': (-1,0),
      'e': (0,1),
      's': (1,0),
      'w': (0,-1)
    }

g_puzzle = [
        ['J', 'A', 'N', 'S', 'N', 'Y', 'E', 'P', 'A', 'R', 'G', 'X'], 
        ['I', 'P', 'V', 'O', 'O', 'R', 'A', 'N', 'G', 'E', 'V', 'T'], 
        ['W', 'P', 'K', 'V', 'L', 'R', 'P', 'M', 'E', 'C', 'U', 'A'], 
        ['I', 'L', 'U', 'E', 'R', 'E', 'M', 'A', 'A', 'M', 'N', 'G'], 
        ['K', 'E', 'M', 'D', 'U', 'B', 'M', 'I', 'P', 'A', 'I', 'A'], 
        ['S', 'O', 'O', 'U', 'S', 'E', 'Y', 'R', 'N', 'A', 'G', 'L'], 
        ['N', 'U', 'J', 'Y', 'M', 'U', 'M', 'A', 'E', 'M', 'Y', 'R'], 
        ['P', 'P', 'B', 'E', 'L', 'L', 'B', 'I', 'J', 'T', 'H', 'A'], 
        ['P', 'V', 'G', 'N', 'N', 'B', 'M', 'J', 'F', 'H', 'A', 'W'], 
        ['J', 'X', 'H', 'O', 'F', 'A', 'M', 'S', 'X', 'R', 'M', 'W'], 
        ['D', 'P', 'W', 'I', 'P', 'P', 'X', 'F', 'G', 'Z', 'Z', 'P'], 
        ['M', 'E', 'B', 'Q', 'W', 'Z', 'C', 'M', 'M', 'S', 'J', 'L']
    ]

g_dictword = ['APPLE', 'BANANA', 'BLUEBERRY', 'GRAPE', 'KIWI', 'LEMON', 'LIME', 'ORANGE', 'PAPAYA', 'WATERMELON']

def print_puzzle(p_puzzle):
    for row in p_puzzle:
        for col in row: 
            print(col.rjust(3),end='')
        print()

def show_puzzle(p_y, p_x, p_dir, p_word):
    print('{} @{},{} Direction:{}'.format(p_word, p_y, p_x, p_dir))
    # clone the puzzle
    puz = [x[:] for x in g_puzzle]
    locs = get_all_locations(p_y, p_x, p_dir)
    for y,x in locs[:len(p_word)]:
        puz[y][x] = '*' + puz[y][x]
    print_puzzle(puz)


def get_next_location(p_y, p_x, p_dir):
    y_incr, x_incr = g_incr[p_dir]
    return

def get_all_locations(p_y, p_x, p_dir):
    get_next_location(p_y, p_x, )
    return

def get_all_letters(p_y, p_x, p_dir):
    return

def search_word(p_y, p_x, p_dir, p_min=MIN_LEN):
    return

def transpose_puzzle():
    # clone the puzzle
    ret = [x[:] for x in g_puzzle]
    # return the puzzle in transpose format
    return list(zip(*ret))

def main():
    sz_across = len(g_puzzle[0])
    sz_down = len(g_puzzle)
    for row in range(sz_down):
        for col in range(sz_across):
            for dir in g_dir:
                search_word(row, col, dir)


if __name__ == '__main__':
    main()