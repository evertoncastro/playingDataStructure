import inquirer
import random
import re
from inquirer.themes import GreenPassion
from tree import Tree

if __name__ == '__main__':
    pattern_validation = re.compile("^([0-9]+)+$")

    questions = [
        inquirer.Text('size', message="What's the node quantity for the tree?")
    ]
    answers = inquirer.prompt(questions, theme=GreenPassion())
    size = int(answers['size'])

    # Random with non-repeated
    random_values = random.sample(xrange(1, 99), size)

    tree = Tree()
    for val in random_values:
        tree.add_value(val)

    tree.traverse_in_order()
    tree.traverse_pre_order()
    tree.traverse_post_order()

