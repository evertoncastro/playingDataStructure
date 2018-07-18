import inquirer
import random
import re
from inquirer.themes import GreenPassion
from tree import Tree

if __name__ == '__main__':

    questions = [
        inquirer.Text('size', message="What's the node quantity for the tree?")
    ]
    answers = inquirer.prompt(questions, theme=GreenPassion())
    size = int(answers['size'])

    # TODO: accept only 1 - 99 as tree size

    # Random with non-repeated
    random_values = random.sample(xrange(1, 99), size)

    tree = Tree()
    for val in random_values:
        tree.add_value(val)

    tree.traverse_in_order()
    tree.traverse_pre_order()
    tree.traverse_post_order()

    flow = True
    while flow:
        questions = [
            inquirer.List('action',
                          message="What action do you want to perform?",
                          choices=['Traverse in order',
                                   'Traverse pre order',
                                   'Traverse post order',
                                   'Exit'],
                          ),
        ]

        answer = inquirer.prompt(questions)

        if answer['action'] == 'Traverse in order':
            tree.traverse_in_order()
        elif answer['action'] == 'Traverse pre order':
            tree.traverse_pre_order()
        elif answer['action'] == 'Traverse post order':
            tree.traverse_post_order()
        elif answer['action'] == 'Exit':
            flow = False


