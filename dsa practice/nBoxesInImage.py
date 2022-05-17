


def q2(image):

    def determine_rectangle(row, col):
        col_copy = col
        row_copy = row
        coordinates = [[row, col]]
        for row in range(len(image)):
            for col in range(len(image[row])):
                while image[row][col_copy + 1] == 0:
                    col_copy += 1
                while image[row_copy + 1][col_copy] == 0:
                    row_copy += 1
        coordinates.append([row_copy, col_copy])
        return coordinates

    def convert_rectangle(coordinates):
        start_row = coordinates[0][0]
        start_col = coordinates[0][1]
        end_row = coordinates[1][0]
        end_col = coordinates[1][1]

        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                image[row][col] = 1

    ans = []
    for row in range(len(image)):
        for col in range(len(image[row])):
            if image[row][col] == 0:
                coordinates = determine_rectangle(row, col)
                ans.append(coordinates)
                convert_rectangle(coordinates)
    return ans




image = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]

print(q2(image))