# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr_val = board[r][c]

                if curr_val != '.':
                    box_coord = f'{r//3},{c//3}'

                    if curr_val in row[r] or curr_val in col[c] or curr_val in box[box_coord]: return False

                    row[r].add(curr_val)
                    col[c].add(curr_val)
                    box[box_coord].add(curr_val)

        return True