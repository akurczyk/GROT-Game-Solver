# https://gist.github.com/sargo/8c75ba58790b230fcf08
import copy


def solve_grot(board_matrx):
    """Return coordinates of the best start point on 'board_matrix' of GROT game."""

    def count_path_len(row_num, col_num):
        """Return the number of elements in the path that starts in ('row_num', 'col_num')."""
        board_matrix_copy = copy.deepcopy(board_matrx)  # We need it so we can remove visited items from the board
        len_ = 0  # Variable that holds the current path length

        while True:
            current_element = board_matrix_copy[row_num][col_num]
            if not current_element:  # We have reached the end of the path (an empty element)
                break

            len_ += 1  # Increment the path length
            board_matrix_copy[row_num][col_num] = None  # Remove the visited element from the board

            # 'current_element' describes out next move
            if current_element == 'u' and row_num != 0:  # If moving Upward and not on the upper edge of the board...
                row_num -= 1  # ...change the coordinates accordingly.
            elif current_element == 'd' and row_num != 3:  # And so on...
                row_num += 1
            elif current_element == 'l' and col_num != 0:
                col_num -= 1
            elif current_element == 'r' and col_num != 3:
                col_num += 1

        return len_

    path_lens = []  # List that stores every possible paths along with its lengths and coordinates
    for row_num, row in enumerate(board_matrx):  # For every row ...
        for col_num, cell in enumerate(row):  # ... and for every cell ...
            path_len = count_path_len(row_num, col_num)  # ... evaluate the path length ...
            path_lens.append((path_len, (row_num, col_num)))  # ... and sore the result along with its coordinates.

    path_lens.sort(reverse=True)  # Sort the list described above by first tuple element (path length)
    best_path = path_lens[0]  # Get the longest possible path (first element on sorted list)
    return best_path[1]  # Return only the coordinates, no path length


if __name__ == '__main__':
    sample_input = [
        ['u', 'd', 'u', 'u'],  # ↑ ↓ ↑ ↑
        ['u', 'r', 'l', 'l'],  # ↑ → ← ←
        ['u', 'u', 'l', 'u'],  # ↑ ↑ ← ↑
        ['l', 'd', 'u', 'l'],  # ← ↓ ↑ ←
    ]
    print(solve_grot(sample_input))
