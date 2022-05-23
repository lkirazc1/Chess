import pygame, random, time
pygame.init()

nothing = 0
knight = 2.5
king = 8000
queen = 9
pawn = 1
bishop = 3
rook = 5
bknight = -2.5
bking = -8000
bqueen = -9
bpawn = -1
brook = 5
bbishop = -3
black = 1
white = -1




class Board:
    def __init__(self):
        self.positions = [[brook, bknight, bbishop, bqueen, bking, bbishop, bknight, brook], [bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn], [nothing, nothing, nothing, nothing, nothing, nothing, nothing, nothing], [nothing, nothing, nothing, nothing, nothing, nothing, nothing, nothing], [nothing, nothing, nothing, nothing, nothing, nothing, nothing, nothing], [nothing, nothing, nothing, nothing, nothing, nothing, nothing, nothing], [pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn], [rook, knight, bishop, queen, king, bishop, knight, rook]]
        self.turn = -1
        self.captures = self.possible_captures_white()  # list of tuples with coordinates of color pieces
        #white is -1 and black is 1



    def possible_captures_white(self):
        possible_black = [brook, bknight, bbishop, bqueen, bpawn]
        black_positions = []
        for i, row in enumerate(self.positions):
            for j, val in enumerate(row):
                if val in possible_black:
                    black_positions.append((i, j))
        return black_positions

    def possible_captures_black(self):
        possible_white = [rook, knight, bishop, queen, pawn]
        white_positions = []
        for i, row in enumerate(self.positions):
            for j, val in enumerate(row):
                if val in possible_white:
                    white_positions.append((i, j))
        
        return white_positions


    
    def knight_movement(self, knight_position):
        row = knight_position[0]
        col = knight_position[1]

        possible_movements = [(row - 2, col - 1), (row - 2, col + 1), (row - 1, col + 2), (row + 1, col + 2), (row + 2, col - 1), (row + 2, col + 1), (row - 1, col - 2), (row + 1, col - 2)]
    
        i = 0
        while i < len(possible_movements):
            if possible_movements[i][0] < 0 or possible_movements[i][1] < 0 or possible_movements[i][0] >= 8 or possible_movements[i][1] >= 8:
                possible_movements.pop(i)
                i -= 1
            elif self.positions[possible_movements[i][0]][possible_movements[i][1]] != nothing and (possible_movements[i][0], [possible_movements[i][1]]) not in self.captures:
                possible_movements.pop(i)
                i -= 1 

            i += 1
        return possible_movements

    def rook_movement(self, rook_position):
        row = rook_position[0]
        col = rook_position[1]

        possible_movements = []
        # horizontal movement

        for c in range(col + 1, 8):
            if (row, c) in self.captures:
                possible_movements.append((row, c))
                break
            elif self.positions[row][c] != nothing:
                break
            possible_movements.append((row, c))
        
        for c in range(col - 1, -1, -1):
            if (row, c) in self.captures:
                possible_movements.append((row, c))
            elif self.positions[row][c] != nothing:
                break
            possible_movements.append((row, c))

        # vertical movement

        for r in range(row + 1, 8):
            if (r, col) in self.captures:
                possible_movements.append((r, col))
                break
            elif self.positions[r][col] != nothing:
                break
            possible_movements.append((r, col))


        for r in range(row - 1, -1, -1):
            if (r, col) in self.captures:
                possible_movements.append((r, col))
                break
            elif self.positions[r][col] != nothing:
                break
            possible_movements.append((r, col))

        return possible_movements

    def bishop_movement(self, bishop_position):
        row = bishop_position[0]
        col = bishop_position[1]

        possible_movements = []

        # iterate through diagonals +1 +1 from top left to bottom right

        r = row + 1
        c = col + 1
        while r < 8 and c < 8:
            if self.positions[r][c] != nothing and (r, c) in self.captures:
                possible_movements.append((r, c))
                break
            elif self.positions[r][c] != nothing:
                break

            possible_movements.append((r, c))
            r += 1
            c += 1

        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if self.positions[r][c] != nothing and (r, c) in self.captures:
                possible_movements.append((r, c))
                break
            elif self.positions[r][c] != nothing:
                break
            possible_movements.append((r, c))
            r += 1
            c += 1
        
        # iterate through diagonals - 1 + 1 and + 1 - 1 from top right to bottom left

        r = row - 1
        c = col + 1
        while r >= 0 and c < 8:
            if self.positions[r][c] != nothing and (r, c) in self.captures:
                possible_movements.append((r, c))
                break
            elif self.positions[r][c] != nothing:
                break
            possible_movements.append((r, c))
            r -= 1
            c += 1

        r = row + 1
        c = col - 1
        while r < 8 and c >= 0:
            if self.positions[r][c] != nothing and (r, c) in self.captures:
                possible_movements.append((r, c))
                break
            elif self.positions[r][c] != nothing:
                break
            possible_movements.append((r, c))
            r += 1
            c -= 1

        return possible_movements


    def queen_movement(self, queen_position):
        
        row = queen_position[0]
        col = queen_position[1]

        possible_movements = []

        # find possible movements for horizontal movement

        for c in range(col + 1, 8):
            if (row, c) in self.captures:
                possible_movements.append((row, c))
                break
            elif self.positions[row][c] != nothing:
                break

            possible_movements.append((row, c))
        
        for c in range(col - 1, -1, -1):
            if (row, c) in self.captures:
                possible_movements.append((row, c))
                break
            elif self.positions[row][c] != nothing:
                break
            possible_movements.append((row, c))
        
        # find possible movements for vertical movements

        for r in range(row + 1, 8):
            if (r, col) in self.captures:
                possible_movements.append((r, col))
                break

            elif self.positions[r][col] != nothing:
                break
            possible_movements.append((r, col))

        for r in range(row - 1, -1, -1):
            if (r, col) in self.captures:
                possible_movements.append((r, col))
                break
            elif self.positions[r][col] != nothing:
                break
            possible_movements.append((r, col))
        


    def pawn_movement(self, pawn_position):
        row = pawn_position[0]
        col = pawn_position[1]








