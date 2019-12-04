class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        return(
            [[int(split_row) for split_row in row_string.split()] for row_string in self.matrix_string.splitlines()][index-1]
        )

    def column(self, index):
        rows = [[int(split_row) for split_row in row_string.split()] for row_string in self.matrix_string.splitlines()]
        columns = [list(t) for t in zip(*rows)]
        return columns[index-1]
