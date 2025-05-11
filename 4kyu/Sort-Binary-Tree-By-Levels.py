# 4 kyu Sort binary tree by levels
# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python


class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n


def tree_by_levels(root):
	result = []
	working_list = []
	if root: working_list.insert(0, root)
	while working_list:
		for i in range(len(working_list)):
			node = working_list.pop(0)
			if node:
				result.append(node.value)
				if node.left:
					working_list.append(node.left)
				if node.right:
					working_list.append(node.right)

	return result


if __name__ == '__main__':
	print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])