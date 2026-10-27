from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(inorder_traversal(root))  # [1, 3, 2]
    print(inorder_traversal(None))  # []
    print(inorder_traversal(TreeNode(1)))  # [1]
