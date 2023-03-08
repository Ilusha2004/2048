import enum
from Field import Field

class Direction(enum.Enum):
    right = 'd',
    left = 'a',
    up = 'w'
    down = 's'

class Turning():

    def __init__(self, field) -> None:
        self.field = field

    def compress(self, field : list) -> tuple[list, bool]:

        # bool variable to determine
        # any change happened or not
        changed = False

        # empty grid
        new_mat : list = []

        # with all cells empty
        for i in range(4):
            new_mat.append([0] * 4)

        # here we will shift entries
        # of each cell to it's extreme
        # left row by row
        # loop to traverse rows
        for i in range(4):
            pos = 0

            # loop to traverse each column
            # in respective row
            for j in range(4):
                if(field[i][j] != 0):

                    # if cell is non empty then
                    # we will shift it's number to
                    # previous empty cell in that row
                    # denoted by pos variable
                    new_mat[i][pos] = field[i][j]

                    if j != pos:
                        changed = True

                    pos += 1

        # returning new compressed matrix
        # and the flag variable.
        return new_mat, changed

    # function to merge the cells
    # in matrix after compressing
    def merge(self, field : list) -> tuple[list, bool]:

        changed = False

        for i in range(4):
            for j in range(4):

                # if current cell has same value as
                # next cell in the row and they
                # are non empty then
                if field[i][j] != 0 and field[i][j] == field[i][j - 1]:

                    # double current cell value and
                    # empty the next cell
                    field[i][j] = field[i][j] * 2
                    field[i][j - 1] = 0

                    # make bool variable True indicating
                    # the new grid after merging is
                    # different.
                    changed = True

        return field, changed

    # function to reverse the matrix
    # means reversing the content of
    # each row (reversing the sequence)
    def reverse(self, field : list) -> list:

        new_mat : list = []

        for i in range(4):
            new_mat.append([])
            for j in range(4):
                number = field[i][3 - j]
                new_mat[i].append(number)

        return new_mat

    # function to get the transpose
    # of matrix means interchanging
    # rows and column
    def transpose(self, field : list) -> list:

        new_mat : list = []

        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(field[j][i])

        return new_mat

    def Status(self) -> str:

        for i in range(4):
            for k in range(4):
                if self.field[i][k] == 2048:
                    print("Win")
                    return 'WIN'

        for i in range(4):
            for k in range(4):
                if self.field[i][k] == 0:
                    print("Con")
                    return 'GAME NOT OVER'

        for i in range(4):
            for k in range(4):
                if self.field[i][k] == self.field[i + 1][k] or self.field[i][k] == self.field[i][k + 1]:
                    print("Con")
                    return 'GAME NOT OVER'

        for k in range(4):
            if self.field[3][k] == self.field[3][k + 1]:
                print("Con")
                return 'GAME NOT OVER'

        for i in range(4):
            if self.field[i][3] == self.field[i + 1][3]:
                print("Con")
                return 'GAME NOT OVER'

        return "fail"


class Movement:

    def __init__(self, field : list):
        self.field = field

    # function to update the matrix
    # if we move / swipe left
    def move_left(self, grid : list) -> tuple[list, bool]:

        turn = Turning(grid)
        # first compress the grid
        new_grid, changed1 = turn.compress(grid)

        # then merge the cells.
        new_grid, changed2 = turn.merge(new_grid)

        changed = changed1 or changed2

        # again compress after merging.
        new_grid, temp = turn.compress(new_grid)

        # return new matrix and bool changed
        # telling whether the grid is same
        # or different
        return new_grid, changed

    # function to update the matrix
    # if we move / swipe right
    def move_right(self, grid : list) -> tuple[list, bool]:

        turn = Turning(grid)
        mov = Movement(grid)
        # to move right we just reverse
        # the matrix
        new_grid : list = turn.reverse(grid)

        # then move left
        new_grid, changed = mov.move_left(new_grid)

        # then again reverse matrix will
        # give us desired result
        new_grid = turn.reverse(new_grid)

        return new_grid, changed

    # function to update the matrix
    # if we move / swipe up
    def move_up(self, grid : list):

        turn = Turning(grid)
        mov = Movement(grid)
        # to move up we just take
        # transpose of matrix
        new_grid : list = turn.transpose(grid)

        # then move left (calling all
        # included functions) then
        new_grid, changed = mov.move_left(new_grid)

        # again take transpose will give
        # desired results
        new_grid = turn.transpose(new_grid)

        return new_grid, changed

    # function to update the matrix
    # if we move / swipe down
    def move_down(self, grid : list):

        turn = Turning(grid)
        mov = Movement(grid)
        # to move down we take transpose
        new_grid : list = turn.transpose(grid)

        # move right and then again
        new_grid, changed = mov.move_right(new_grid)

        # take transpose will give desired
        # results.
        new_grid = turn.transpose(new_grid)

        return new_grid, changed