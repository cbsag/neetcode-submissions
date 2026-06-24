class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        print(rows,cols,boxes)
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                # print(r, c, board[r][c])
                # print(value)
                box_index = (r // 3) * 3 + (c // 3)
                print(r, c, board[r][c], "box:", box_index)
                if value == ".":
                    continue
                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[box_index]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        return True