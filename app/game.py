class Direction:
    """
    Helper class to implement enum type for
    direction.
    """
    NORTH    = 0
    SOUTH    = 180
    EAST     = 90
    WEST     = 270

    strlookup = { NORTH: 'N',
                  SOUTH: 'S',
                  EAST: 'E',
                  WEST: 'W' }

class Board:
    """
    Class representing an X by Y board with
    a single piece.
    """
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.piece = Piece()

    def validMove(self, x, y):
        """
        Check whether a moving a piece results in a valid
        move, if the move would result in piece moving off
        the board return false.
        """
        if x < self.width and x >= 0 and y< self.height and y >= 0:
            return True
        else:
            return False

    def movePiece(self, command):
        """
        Move a piece based on a string of commands, the syntax
        for the commands is:
        M - move the piece forward 1 place in the direction it is
            pointing
        R - rotate the piece clockwise
        L - rotate the piece anti-clockwise

        The code assumes a correctly formed command made up of the
        characters M,R,L and walks through each command in the
        string passing it to the piece move function.
        """
        for c in command:
            x, y = self.piece.move(c)
            if self.validMove(x, y):
                self.piece.x = x
                self.piece.y = y

        return ("%s %s %s" % (self.piece.x, self.piece.y,
            Direction.strlookup[self.piece.direction])) 

class Piece:
    """
    Class representing a game piece, takes the starting
    x, y location for the piece defaulting to 0,0. It
    has a default direction of North.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = Direction.NORTH 

    def move(self,command):
        """
        Function to move a piece based on a command, the
        command is either:

        M - move piece forward
        R - rotate piece clockwise
        L - rotate piece anti-clockwise
        """
        x = 0
        y = 0
        if command == 'M':
            if self.direction == Direction.NORTH:
                x = self.x
                y = self.y+1
            if self.direction == Direction.EAST:
                x = self.x + 1
                y = self.y
            if self.direction == Direction.SOUTH:
                x = self.x
                y = self.y - 1
            if self.direction == Direction.WEST:
                x = self.x - 1
                y = self.y
        if command == 'R':
            self.direction = (self.direction + 90) % 360
            x = self.x
            y = self.y
        if command == 'L':
           self.direction = (self.direction - 90) % 360
           x = self.x
           y = self.y

        return (x, y)

    def set_direction(self,direction):
        """
        Set the direction of the piece.
        """
        self.direction = direction

def main(): #pragma: no cover
    board = Board(5,5)

    while True:
        cmd = raw_input()

        print board.movePiece(cmd)

if __name__ == "__main__": #pragma: no cover
    main()
