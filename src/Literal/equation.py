# import library
from src.Trees.trees import BinaryTree
from src.Trees.calculator import calculate_tree
from turtle import Turtle, done


class Equation:
    """
    Class to solve an equation
    """

    # init the equation
    def __init__(self, x):
        self.unknown = x

    def resolve(self, left: BinaryTree, right: BinaryTree = 0) -> list:

        """
        Resolve the equation

        params:
        left (BinaryTree): The left part of the equation
        right (BinaryTree): The right part of the equation

        result (list): solution(s) of the equation
        """
        assert self.__verif(left, right), 'Tree is empty'

        # init all unknowns in the equation
        all_x = 0

        # init the result
        result = None

        # init the check (niveau 1)
        check = 1

        # check if the equation is simple ('+' or '-' or '*') and add the unknowns
        for side in [left, right]:
            for branch in side.iter_branches():
                if branch.value == self.unknown:
                    all_x += 1 if side == left else -1
                elif branch.value == '*':
                    if branch.left.value == self.unknown:
                        all_x += branch.right.value if side == left else -branch.right.value
                        branch.left.value = 0
                    elif branch.right.value == self.unknown:
                        all_x += branch.left.value if side == left else -branch.left.value
                        branch.right.value = 0
                elif not isinstance(branch.value, (int, float)) and branch.value not in ['+', '-','*', self.unknown]:
                    check = 2

        if check == 1:
            result = self.niveau_1(left, right, all_x)

        return result

    def niveau_1(self, left: BinaryTree, right: BinaryTree, all_x: int) -> list:
        """
        Solve the equation if it is simple
        """
        print('niveau 1')
        if all_x == 0:
            raise Exception(f'No {self.unknown} in the equation or {self.unknown} cancels out')

        solutions = []

        # replace the unknown variable by 0
        self.__replace(left, self.unknown, 0)
        self.__replace(right, self.unknown, 0)

        # calculate the result
        result_left = -calculate_tree(left)
        result_right = calculate_tree(right)
        result = result_left + result_right

        # verify if is unknown is negative
        if all_x < 0:
            result = -result
            all_x = -all_x

        result /= all_x

        # add the result to the list
        solutions.append(result)

        return solutions

    def __find_x(self, arbre: BinaryTree, v: int = 1) -> list:
        """
        Find the unknown variable in the equation
        """
        k = 1
        for i in arbre.iter_branches():
            if not i.is_leaf() and i.left.value == self.unknown or i.right.value == self.unknown:
                if k == v:
                    return i
                k += 1

    def __replace(self, arbre: BinaryTree, x, y):
        """
        Replace the value of the unknown variable by the value given (0)
        """
        for i in arbre.iter_branches():
            if i.value == x:
                i.value = y

    def __verif(self, left: BinaryTree, right: BinaryTree) -> bool:
        """
        Check if the equation is simple

        :param arbre: The equation
        :return: basic verification
        """
        return not (left is None or right is None)


if __name__ == '__main__':
    branch_left = BinaryTree('+').set_branches(BinaryTree('*').set_branches(4, 'x'), BinaryTree('-').set_branches(3, 6))
    branch_right = BinaryTree('+').set_branches('x', 1)
    print("left tree : ", branch_left)
    print("right tree :", branch_right)

    eq = Equation('x')
    print("solution(s):", eq.resolve(branch_left, branch_right))

    # branch_right
    t = Turtle()
    t.penup()
    t.goto(0, 350)
    branch_right.draw(t)
    done()
