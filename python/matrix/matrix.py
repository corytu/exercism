class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(split_row) for split_row in row_string.split()] for row_string in matrix_string.splitlines()]

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        columns = [list(t) for t in zip(*self.rows)]
        return columns[index-1]
