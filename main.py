# Hexagonal board map: 9 rows (a-i), 61 tiles total.
# Each value is a list: [stone_marker, neighbor1/void, neighbor2/void, ...]
# stone_marker starts empty ("") and can be set later to mark a stone.
dirmap = {
    'a1': ['', 'void', 'a2', 'void', 'void', 'b1', 'b2'],
    'a2': ['', 'a1', 'a3', 'void', 'void', 'b2', 'b3'],
    'a3': ['', 'a2', 'a4', 'void', 'void', 'b3', 'b4'],
    'a4': ['', 'a3', 'a5', 'void', 'void', 'b4', 'b5'],
    'a5': ['', 'a4', 'void', 'void', 'void', 'b5', 'b6'],
    'b1': ['', 'void', 'b2', 'void', 'a1', 'c1', 'c2'],
    'b2': ['', 'b1', 'b3', 'a1', 'a2', 'c2', 'c3'],
    'b3': ['', 'b2', 'b4', 'a2', 'a3', 'c3', 'c4'],
    'b4': ['', 'b3', 'b5', 'a3', 'a4', 'c4', 'c5'],
    'b5': ['', 'b4', 'b6', 'a4', 'a5', 'c5', 'c6'],
    'b6': ['', 'b5', 'void', 'a5', 'void', 'c6', 'c7'],
    'c1': ['', 'void', 'c2', 'void', 'b1', 'd1', 'd2'],
    'c2': ['', 'c1', 'c3', 'b1', 'b2', 'd2', 'd3'],
    'c3': ['', 'c2', 'c4', 'b2', 'b3', 'd3', 'd4'],
    'c4': ['', 'c3', 'c5', 'b3', 'b4', 'd4', 'd5'],
    'c5': ['', 'c4', 'c6', 'b4', 'b5', 'd5', 'd6'],
    'c6': ['', 'c5', 'c7', 'b5', 'b6', 'd6', 'd7'],
    'c7': ['', 'c6', 'void', 'b6', 'void', 'd7', 'd8'],
    'd1': ['', 'void', 'd2', 'void', 'c1', 'e1', 'e2'],
    'd2': ['', 'd1', 'd3', 'c1', 'c2', 'e2', 'e3'],
    'd3': ['', 'd2', 'd4', 'c2', 'c3', 'e3', 'e4'],
    'd4': ['', 'd3', 'd5', 'c3', 'c4', 'e4', 'e5'],
    'd5': ['', 'd4', 'd6', 'c4', 'c5', 'e5', 'e6'],
    'd6': ['', 'd5', 'd7', 'c5', 'c6', 'e6', 'e7'],
    'd7': ['', 'd6', 'd8', 'c6', 'c7', 'e7', 'e8'],
    'd8': ['', 'd7', 'void', 'c7', 'void', 'e8', 'e9'],
    'e1': ['', 'void', 'e2', 'void', 'd1', 'void', 'f1'],
    'e2': ['', 'e1', 'e3', 'd1', 'd2', 'f1', 'f2'],
    'e3': ['', 'e2', 'e4', 'd2', 'd3', 'f2', 'f3'],
    'e4': ['', 'e3', 'e5', 'd3', 'd4', 'f3', 'f4'],
    'e5': ['', 'e4', 'e6', 'd4', 'd5', 'f4', 'f5'],
    'e6': ['', 'e5', 'e7', 'd5', 'd6', 'f5', 'f6'],
    'e7': ['', 'e6', 'e8', 'd6', 'd7', 'f6', 'f7'],
    'e8': ['', 'e7', 'e9', 'd7', 'd8', 'f7', 'f8'],
    'e9': ['', 'e8', 'void', 'd8', 'void', 'f8', 'void'],
    'f1': ['', 'void', 'f2', 'e1', 'e2', 'void', 'g1'],
    'f2': ['', 'f1', 'f3', 'e2', 'e3', 'g1', 'g2'],
    'f3': ['', 'f2', 'f4', 'e3', 'e4', 'g2', 'g3'],
    'f4': ['', 'f3', 'f5', 'e4', 'e5', 'g3', 'g4'],
    'f5': ['', 'f4', 'f6', 'e5', 'e6', 'g4', 'g5'],
    'f6': ['', 'f5', 'f7', 'e6', 'e7', 'g5', 'g6'],
    'f7': ['', 'f6', 'f8', 'e7', 'e8', 'g6', 'g7'],
    'f8': ['', 'f7', 'void', 'e8', 'e9', 'g7', 'void'],
    'g1': ['', 'void', 'g2', 'f1', 'f2', 'void', 'h1'],
    'g2': ['', 'g1', 'g3', 'f2', 'f3', 'h1', 'h2'],
    'g3': ['', 'g2', 'g4', 'f3', 'f4', 'h2', 'h3'],
    'g4': ['', 'g3', 'g5', 'f4', 'f5', 'h3', 'h4'],
    'g5': ['', 'g4', 'g6', 'f5', 'f6', 'h4', 'h5'],
    'g6': ['', 'g5', 'g7', 'f6', 'f7', 'h5', 'h6'],
    'g7': ['', 'g6', 'void', 'f7', 'f8', 'h6', 'void'],
    'h1': ['', 'void', 'h2', 'g1', 'g2', 'void', 'i1'],
    'h2': ['', 'h1', 'h3', 'g2', 'g3', 'i1', 'i2'],
    'h3': ['', 'h2', 'h4', 'g3', 'g4', 'i2', 'i3'],
    'h4': ['', 'h3', 'h5', 'g4', 'g5', 'i3', 'i4'],
    'h5': ['', 'h4', 'h6', 'g5', 'g6', 'i4', 'i5'],
    'h6': ['', 'h5', 'void', 'g6', 'g7', 'i5', 'void'],
    'i1': ['', 'void', 'i2', 'h1', 'h2', 'void', 'void'],
    'i2': ['', 'i1', 'i3', 'h2', 'h3', 'void', 'void'],
    'i3': ['', 'i2', 'i4', 'h3', 'h4', 'void', 'void'],
    'i4': ['', 'i3', 'i5', 'h4', 'h5', 'void', 'void'],
    'i5': ['', 'i4', 'void', 'h5', 'h6', 'void', 'void'],
}

def fill_starting_position(emap):
    for key in emap:
        if key.startswith('a') or key.startswith('b') or key in {'c3', 'c4', 'c5'}:
            emap[key][0] = 0
        if key.startswith('h') or key.startswith('i') or key in {'g3', 'g4', 'g5'}:
            emap[key][0] = 1
    return emap

def check_possible_moves(cmap, player):
    movemap = {}
    for key in cmap:
        values = cmap[key]
        if values[0] == player:
            movemap[key] = []
            for direction in range(1, len(values)):
               if not values[direction] == 'void':
                    nextpos = values[direction]
                    if cmap[nextpos][0] == '':
                        #Wenn zugrichtung leer ist wird zug als möglich angehangen
                        movemap[key].append(values[direction])
                    elif cmap[nextpos][0] == player:
                        #Wenn eigner im weg dann kein zug möglich
                        pass
                    elif cmap[nextpos][0] == abs(player-1):
                        #Wenn Gegner da ist muss zuerst kraft welche wirkt und mögliche schwarze blockade bestimmt werden um legalität zu testen
                        nextpos2 = cmap[nextpos[direction]]
                        if nextpos2 == 'void' or cmap[nextpos2][0] == '':
                            strength = 1
                        elif cmap[nextpos2][0] == player:
                            pass
                        else:
                            nextpos3 = cmap[nextpos2.value()[direction]]
                            if nextpos3 == 'void' or cmap[nextpos3][0] == '':
                                strength = 2
                            elif cmap[nextpos3][0] == player:
                                pass
                        if strength == {1, 2}:
                        #Stärke von aktivem player herausfinden
                            oppositedirection = (direction + 3)
                            if oppositedirection > 6:
                                oppositedirection -= 6
                            behindpos = values[oppositedirection]
                            if cmap[behindpos][0] == player:
                                if strength == 1:
                                    movemap[key].append(values[direction])
                                else:
                                    if cmap[cmap[behindpos][oppositedirection]][0] == player: #wenn der dritte vorher aus schwarz ist dann muss zwangsläufig auch gültig sein
                                        movemap[key].append(values[direction])


    return movemap

def finddirectionindex(key, value):
    return dirmap[key].index(value) 
       



#MAIN
workmap = fill_starting_position(dirmap)
print(check_possible_moves(workmap, 0))
