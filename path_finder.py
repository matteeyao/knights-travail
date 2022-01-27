from tree import Node


class KnightPathFinder:
    # __slots__ = ['_root', '_considered_positions']

    def __init__(self, pos):
        self._root = Node(pos)
        self._considered_positions = {pos, }
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
            if new_x in range(8) and new_y in range(8):
                moves.append(new_pos)

        return moves

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        filtered_moves = set(valid_moves) - self._considered_positions
        self._considered_positions = self._considered_positions | set(valid_moves)
        return filtered_moves

    def build_move_tree(self):
        queue = [self._root]

        while queue:
            current_node = queue.pop(0)
            new_moves = self.new_move_positions(current_node.value)
            for new_move in new_moves:
                child = Node(new_move)
                current_node.add_child(child)
                queue.append(child)

    def find_path(self, end_position):
        end_node = self._root.depth_search(end_position)
        path = [node.value for node in self.trace_to_root(end_node)]
        return path

    def trace_to_root(self, end_node):
        path_list = []
        current_node = end_node
        while current_node:
            path_list.append(current_node)
            current_node = current_node.parent
        return path_list[::-1]


# Phase II:

# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))                # → {(1, 2), (2, 1)}

# Phase III:

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)                            # → [<tree.Node object at 0x108fc6520>, <tree.Node object at 0x108fc6850>]

# Phase IV:

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder.find_path((2, 1)))                         #  → [(0, 0), (2, 1)]
# print(finder.find_path((3, 3)))                         #  → [(0, 0), (2, 1), (3, 3)]
# print(finder.find_path((6, 2)))                         #  → [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# print(finder.find_path((7, 6)))                         #  → [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
