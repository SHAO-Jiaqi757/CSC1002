
MIN_LEN = 4
g_puzzle = []
g_puzzle_t = []
g_dictword = []
g_dir = ['n','e','s','w','ne','nw','se','sw']
g_incr = {
      'n': (-1,0),
      'e': (0,1),
      's': (1,0),
      'w': (0,-1),
      'ne': (-1,1),
      'se': (1,1),
      'sw': (1,-1),
      'nw': (-1,-1)
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

# print the puzzle on the console
# with each letter 3-character wide, right justified.
def print_puzzle(p_puzzle):
    for row in p_puzzle:
        for col in row: 
            print(col.rjust(3),end='')
        print()

# show given word in the puzzle,
# with each letter prefixed with '*'
def show_word(p_y, p_x, p_dir, p_word):
    print('{} @{},{} Direction:{}'.format(p_word, p_y, p_x, p_dir))
    # clone the puzzle
    puz = [x[:] for x in g_puzzle]
    locs = get_all_locations(p_y, p_x, p_dir)
    for y,x in locs[:len(p_word)]:
        puz[y][x] = '*' + puz[y][x]
    print_puzzle(puz)

# return the next valid location as (row,col) in 
# the given direction and starting position, (-1,-1) otherwise
def get_next_location(p_y, p_x, p_dir):
    y_incr, x_incr = g_incr[p_dir]    
    p_y = p_y + y_incr 
    p_x = p_x + x_incr
    if p_y in range(len(g_puzzle)) and p_x in range(len(g_puzzle[0])):
        return (p_y, p_x)
    return (-1,-1)

# return all locations as list of (row,col)
# in the given direction and starting position (p_y,p_x)
def get_all_locations(p_y, p_x, p_dir):
    
    while True: 
        (p_y, p_x) = get_next_location(p_y, p_x, p_dir)
        if (p_y, p_x) == (-1, -1):
            break        
        g_puzzle_t.append((p_y, p_x))        
    return g_puzzle_t
# return all letters as a string 
# in the given direction and starting position (p_y,p_x) 
def get_all_letters(p_y, p_x, p_dir):
    
    locs = get_all_locations(p_y, p_x, p_dir)
    letters = [g_puzzle[y][x] for y,x in locs]
    return "".join(letters)
# search for hidden word in the given direction
# at location (p_y,p_x)
def search_word(p_y, p_x, p_dir, p_min=MIN_LEN):
    letters = get_all_letters(p_y, p_x, p_dir)
    
    if  letters and len(letters) > p_min:
        for word in g_dictword:
            if letters.find(word) == 0:
                show_word(p_y, p_x, p_dir, word)
            else:
                continue

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
                g_puzzle_t.append((row, col))
                search_word(row, col, dir)
                g_puzzle_t.clear()


if __name__ == '__main__':
    main()
    
    