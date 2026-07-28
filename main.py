# Hexagonal board map: 9 rows (a-i), 61 tiles total.
# Each value is a list: [stone_marker, neighbor1/void, neighbor2/void, ...]
# stone_marker starts empty ("") and can be set later to mark a stone.

dirmap = {
    'a1': ['', 'void', 'void', 'void', 'a2', 'b2', 'b1'],
    'a2': ['', 'a1', 'void', 'void', 'a3', 'b3', 'b2'],
    'a3': ['', 'a2', 'void', 'void', 'a4', 'b4', 'b3'],
    'a4': ['', 'a3', 'void', 'void', 'a5', 'b5', 'b4'],
    'a5': ['', 'a4', 'void', 'void', 'void', 'b6', 'b5'],
    'b1': ['', 'void', 'void', 'a1', 'b2', 'c2', 'c1'],
    'b2': ['', 'b1', 'a1', 'a2', 'b3', 'c3', 'c2'],
    'b3': ['', 'b2', 'a2', 'a3', 'b4', 'c4', 'c3'],
    'b4': ['', 'b3', 'a3', 'a4', 'b5', 'c5', 'c4'],
    'b5': ['', 'b4', 'a4', 'a5', 'b6', 'c6', 'c5'],
    'b6': ['', 'b5', 'a5', 'void', 'void', 'c7', 'c6'],
    'c1': ['', 'void', 'void', 'b1', 'c2', 'd2', 'd1'],
    'c2': ['', 'c1', 'b1', 'b2', 'c3', 'd3', 'd2'],
    'c3': ['', 'c2', 'b2', 'b3', 'c4', 'd4', 'd3'],
    'c4': ['', 'c3', 'b3', 'b4', 'c5', 'd5', 'd4'],
    'c5': ['', 'c4', 'b4', 'b5', 'c6', 'd6', 'd5'],
    'c6': ['', 'c5', 'b5', 'b6', 'c7', 'd7', 'd6'],
    'c7': ['', 'c6', 'b6', 'void', 'void', 'd8', 'd7'],
    'd1': ['', 'void', 'void', 'c1', 'd2', 'e2', 'e1'],
    'd2': ['', 'd1', 'c1', 'c2', 'd3', 'e3', 'e2'],
    'd3': ['', 'd2', 'c2', 'c3', 'd4', 'e4', 'e3'],
    'd4': ['', 'd3', 'c3', 'c4', 'd5', 'e5', 'e4'],
    'd5': ['', 'd4', 'c4', 'c5', 'd6', 'e6', 'e5'],
    'd6': ['', 'd5', 'c5', 'c6', 'd7', 'e7', 'e6'],
    'd7': ['', 'd6', 'c6', 'c7', 'd8', 'e8', 'e7'],
    'd8': ['', 'd7', 'c7', 'void', 'void', 'e9', 'e8'],
    'e1': ['', 'void', 'void', 'd1', 'e2', 'f1', 'void'],
    'e2': ['', 'e1', 'd1', 'd2', 'e3', 'f2', 'f1'],
    'e3': ['', 'e2', 'd2', 'd3', 'e4', 'f3', 'f2'],
    'e4': ['', 'e3', 'd3', 'd4', 'e5', 'f4', 'f3'],
    'e5': ['', 'e4', 'd4', 'd5', 'e6', 'f5', 'f4'],
    'e6': ['', 'e5', 'd5', 'd6', 'e7', 'f6', 'f5'],
    'e7': ['', 'e6', 'd6', 'd7', 'e8', 'f7', 'f6'],
    'e8': ['', 'e7', 'd7', 'd8', 'e9', 'f8', 'f7'],
    'e9': ['', 'e8', 'd8', 'void', 'void', 'void', 'f8'],
    'f1': ['', 'void', 'e1', 'e2', 'f2', 'g1', 'void'],
    'f2': ['', 'f1', 'e2', 'e3', 'f3', 'g2', 'g1'],
    'f3': ['', 'f2', 'e3', 'e4', 'f4', 'g3', 'g2'],
    'f4': ['', 'f3', 'e4', 'e5', 'f5', 'g4', 'g3'],
    'f5': ['', 'f4', 'e5', 'e6', 'f6', 'g5', 'g4'],
    'f6': ['', 'f5', 'e6', 'e7', 'f7', 'g6', 'g5'],
    'f7': ['', 'f6', 'e7', 'e8', 'f8', 'g7', 'g6'],
    'f8': ['', 'f7', 'e8', 'e9', 'void', 'void', 'g7'],
    'g1': ['', 'void', 'f1', 'f2', 'g2', 'h1', 'void'],
    'g2': ['', 'g1', 'f2', 'f3', 'g3', 'h2', 'h1'],
    'g3': ['', 'g2', 'f3', 'f4', 'g4', 'h3', 'h2'],
    'g4': ['', 'g3', 'f4', 'f5', 'g5', 'h4', 'h3'],
    'g5': ['', 'g4', 'f5', 'f6', 'g6', 'h5', 'h4'],
    'g6': ['', 'g5', 'f6', 'f7', 'g7', 'h6', 'h5'],
    'g7': ['', 'g6', 'f7', 'f8', 'void', 'void', 'h6'],
    'h1': ['', 'void', 'g1', 'g2', 'h2', 'i1', 'void'],
    'h2': ['', 'h1', 'g2', 'g3', 'h3', 'i2', 'i1'],
    'h3': ['', 'h2', 'g3', 'g4', 'h4', 'i3', 'i2'],
    'h4': ['', 'h3', 'g4', 'g5', 'h5', 'i4', 'i3'],
    'h5': ['', 'h4', 'g5', 'g6', 'h6', 'i5', 'i4'],
    'h6': ['', 'h5', 'g6', 'g7', 'void', 'void', 'i5'],
    'i1': ['', 'void', 'h1', 'h2', 'i2', 'void', 'void'],
    'i2': ['', 'i1', 'h2', 'h3', 'i3', 'void', 'void'],
    'i3': ['', 'i2', 'h3', 'h4', 'i4', 'void', 'void'],
    'i4': ['', 'i3', 'h4', 'h5', 'i5', 'void', 'void'],
    'i5': ['', 'i4', 'h5', 'h6', 'void', 'void', 'void'],
}


ROWS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
SIZES = [5, 6, 7, 8, 9, 8, 7, 6, 5]
MAX_SIZE = max(SIZES)
 
SYMBOLS = {
    "": "·",   # leer
    1: "○",    # player 0
    0: "●",    # player 1
}

STONECOUNT = {}


def opposite_index(i):
    newindex = (i + 3)
    if newindex > 6:
        newindex -= 6
    return newindex

def fill_starting_position(emap):
    for key in emap:
        if key.startswith(('a', 'b')) or key in {'c3', 'c4', 'c5'}:
            emap[key][0] = 0
        if key.startswith(('h', 'i')) or key in {'g3', 'g4', 'g5'}:
            emap[key][0] = 1
    return emap


def print_board(emap):
    print()
    for letter, size in zip(ROWS, SIZES):
        indent = MAX_SIZE - size          # jeder reihe in die richtige zentrierung
        cells = []
        for i in range(1, size + 1):
            marker = emap[f"{letter}{i}"][0]
            cells.append(SYMBOLS.get(marker, "?"))
        row_str = " ".join(cells)
        print(f"{letter} " + " " * indent + row_str)
    print()
    print("legend:  · empty    ○ player 1    ● player 0")
    print()       


def check_possible_moves(cmap, player):
    singlemap = {}
    queuemap = {}
    pushmap = {}
    for key in cmap:
        values = cmap[key]
        if values[0] == player:
            for direction in range(1, len(values)): #checkt alle richtungen für mögliche moves
               if values[direction] != 'void':
                    nextpos = values[direction]
                    if cmap[nextpos][0] == '': #freies feld: single oder push move möglich
                        if not key in singlemap:
                            singlemap[key] = []
                        singlemap[key].append(dirmap[key][direction])
                        queuelist = (find_queue_moves(cmap, key, direction, player))
                        if len(queuelist) > 0:
                            if not key in queuemap:
                                queuemap[key] = []
                            queuemap[key].extend(queuelist)
                    elif cmap[nextpos][0] == player:
                        #Wenn eigner im weg dann kein zug möglich
                        pass
                    elif cmap[nextpos][0] == abs(player-1):
                        #Wenn Gegner da ist muss zuerst kraft welche wirkt und mögliche eigene blockade bestimmt werden um legalität zu testen
                        pushlist = find_push_moves(cmap, key, direction, player, nextpos, values)
                        if len(pushlist) > 0:
                            pushmap[key] = pushlist
    slidemap = find_slide_moves(cmap, player, singlemap)
    return singlemap, queuemap, pushmap, slidemap

def finddirectionindex(key, value):
    return dirmap[key].index(value) 
       

def find_queue_moves(cmap, key, direction, player):
    movelist = []

    oppositedirection = opposite_index(direction)
   
    behindpos = cmap[key][oppositedirection]
    if behindpos == 'void':
        return movelist
    if cmap[behindpos][0] == player:
        movelist.append([cmap[key][direction], 2])
    if cmap[behindpos][oppositedirection] == 'void':
        return movelist
    if cmap[cmap[behindpos][oppositedirection]][0] == player:
        movelist.append([cmap[key][direction], 3])
    return movelist

def find_push_moves(cmap, key, direction, player, nextpos, values):
    movelist = []
    nextpos2 = dirmap[nextpos][direction]
    if nextpos2 == 'void' or cmap[nextpos2][0] == '': #stärke 1 vom gegner
        strength = 1
    elif cmap[nextpos2][0] == player: #eigene blockade: kein zug möglich
        strength = 0
    else:
        nextpos3 = dirmap[nextpos2][direction]
        if nextpos3 == 'void' or cmap[nextpos3][0] == '':
            strength = 2
        else:
            strength = 0
    if strength in {1, 2}: #jetzt stärke von aktivem player herausfinden
        oppositedirection = opposite_index(direction)
        behindpos = values[oppositedirection]
        if cmap[behindpos] != 'void' and cmap[behindpos][0] == player:
            if strength == 1:
                movelist.append([values[direction], 2])
            if cmap[behindpos][oppositedirection] != 'void' and cmap[cmap[behindpos][oppositedirection]][0] == player: #wenn der dritte vorher aus schwarz ist dann muss zwangsläufig auch gültig sein
                movelist.append([values[direction], 3])
    return movelist

def find_slide_moves(cmap, player, singlemap):
    slidemap = {}
    directions = [1, 2] #muss nur 2 von 4 richtungen für slides checken da die anderen 2 schon vom vorherigen geprüft sind
    for key in singlemap:
        values = singlemap[key]
        for activemove in values:
            operatingdirection = finddirectionindex(key, activemove)
            for direction in directions:
                partnerdirection = operatingdirection + direction
                if partnerdirection > 6:
                    partnerdirection -= 6
                #now we can check if position in partnerdirection has a team stone
                partner1 = cmap[key][partnerdirection]
                if partner1 != 'void' and cmap[partner1][operatingdirection] != 'void' and cmap[partner1][0] == player and cmap[cmap[partner1][operatingdirection]][0] == '': 
                    #jetzt ist 2er slide möglich
                    if not key in slidemap:
                        slidemap[key] = []
                    slidemap[key].append([cmap[key][operatingdirection], partnerdirection, 2])
                    partner2 = cmap[partner1][partnerdirection]
                    if partner2 != 'void' and cmap[partner2][operatingdirection] != 'void' and cmap[partner2][0] == player and cmap[cmap[partner2][operatingdirection]][0] == '': 
                        #jetzt ist 3er slide möglich
                        if not key in slidemap:
                            slidemap[key] = []
                        slidemap[key].append([cmap[key][operatingdirection], partnerdirection, 3])
    return slidemap



def moveselection_manual(cmap, player):
    singlemap, queuemap, pushmap, slidemap = check_possible_moves(cmap, player)
    move_selection = {
            's': singlemap,
            'q': queuemap,
            'p': pushmap,
            'l': slidemap
        }
    movetype = input("Please select a move (s: single, q: queue, p: push, l: slide): ")
    movesquare = input("Please select a square (a1 - i5): ")
    movedirection = input("Please select a direction square (a1 - i5): ")
    movenumber = input("Please select the number of stones, this must match the move type (1, 2, 3): ")
    if movetype == 'l':
        partnerstone = input("Please select the partner stone (a1 - i5): ")
    else:
        partnerstone = None
    if movetype in move_selection and movesquare in move_selection[movetype] and any(movedirection in sublist for sublist in move_selection[movetype][movesquare]) and int(movenumber) in {1, 2, 3}:
        umap = apply_move(cmap, movetype, movesquare, movedirection, movenumber, partnerstone,  player)
        print(print_board(umap))
        return umap
    else:
        print("Invalid input. Please try again.")
        return moveselection_manual(cmap, player)

def apply_move(cmap, movetype, movesquare, movedirection, movenumber, partnerstone, player):
    if movetype == 's':
        return apply_single_move(cmap, movesquare, movedirection, movenumber, player)
    elif movetype == 'q':
        print(movenumber)
        return apply_queue_move(cmap, movesquare, movedirection, movenumber, player)
    elif movetype == 'p':
        return apply_push_move(cmap, movesquare, movedirection, movenumber, player)
    elif movetype == 'l':
        return apply_slide_move(cmap, movesquare, movedirection, movenumber, partnerstone, player)

def apply_single_move(cmap, movesquare, movedirection, movenumber, player):
    cmap[movesquare][0] = ''
    cmap[movedirection][0] = player
    return cmap
def apply_queue_move(cmap, movesquare, movedirection, movenumber, player):
    cmap[movedirection][0] = player
    if movenumber == '2':
        oppositedirection = opposite_index(dirmap[movesquare].index(movedirection))
        cmap[cmap[movesquare][oppositedirection]][0] = ''
    elif movenumber == '3':
        oppositedirection = opposite_index(dirmap[movesquare].index(movedirection))
        cmap[cmap[cmap[movesquare][oppositedirection]][oppositedirection]][0] = ''
        print(cmap[cmap[cmap[movesquare][oppositedirection]][oppositedirection]])
        print(cmap[cmap[cmap[movesquare][oppositedirection]][oppositedirection]][0])
        print(22222)
    return cmap
def apply_push_move(cmap, movesquare, movedirection, movenumber, player):
    direction = dirmap[movesquare].index(movedirection)
    if cmap[movedirection][direction] != 'void' and cmap[cmap[movedirection][direction]][0] == 1-player:
        cmap = apply_queue_move(cmap, movesquare, movedirection, movenumber, player)
        if cmap[cmap[movedirection][direction]][direction] == 'void':
            STONECOUNT[1-player] -= 1
            return cmap
        cmap[cmap[cmap[movedirection][direction]][direction]][0] = 1-player
    else:
        cmap = apply_queue_move(cmap, movesquare, movedirection, movenumber, player)
        if cmap[movedirection][direction] == 'void':
            STONECOUNT[1-player] -= 1
            return cmap
        cmap[cmap[movedirection][direction]][0] = 1-player
    return cmap
def apply_slide_move(cmap, movesquare, movedirection, movenumber, partnerstone, player):
    direction = dirmap[movesquare].index(movedirection)
    partnerdirection = dirmap[movesquare].index(partnerstone)
    cmap[cmap[movesquare][direction]][0] = player
    cmap[cmap[partnerstone][direction]][0] = player
    cmap[movesquare][0] = ''
    cmap[partnerstone][0] = ''
    if movenumber == '3':
        cmap[cmap[cmap[partnerstone][partnerdirection]][direction]][0] = player
        cmap[cmap[partnerstone][partnerdirection]][0] = ''
        return cmap



def main():
    global STONECOUNT
    STONECOUNT= {0: 14, 1: 14}
    workmap = fill_starting_position(dirmap)
    print_board(workmap)
    activeplayer = 0
    while True:
        workmap = moveselection_manual(workmap, activeplayer)
        activeplayer = 1 - activeplayer





if __name__ == "__main__":
    main()
