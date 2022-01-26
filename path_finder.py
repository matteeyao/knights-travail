from tree import Node

class KnightPathFinder:
    __slots__ = ['_root', '_considered_positions']
    def __init__(self, pos):
        self._root=Node(pos)
        self._considered_positions={pos,}
        # self._considered_positions=set(pos) ▶ also works
        
    def get_valid_moves(self, pos):
        possibilities = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        moves = []
        x, y = pos

        for a, b in possibilities:
            new_pos = (x + a, y + b)
            new_x, new_y = new_pos
            moves.append(new_pos)

        return moves

    def new_move_positions(self, pos):
        moves = self.get_valid_moves(pos)
        valid_moves = [pos for pos in moves if pos[0] in range(8) and pos[1] in range(8)]
        filtered_moves = set(valid_moves) - self._considered_positions
        self._considered_positions = self._considered_positions | set(valid_moves)
        return filtered_moves


# Phase II:

# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))                # → {(1, 2), (2, 1)}

# Phase III:



# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)   # [<tree.Node object at 0x108fc6520>, <tree.Node object at 0x108fc6850>]