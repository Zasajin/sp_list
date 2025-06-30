import list as sp_list
import mainframe as mf

def_ctgs = {

    'Kitchen': 0,
    'Gardening': 1,
    'Spices': 2,
    'Fish': 3,
    'Meat': 4,
    'Fruit and Veggie': 5,
    'Vegan': 6,
    'Frozen and Ice': 7,
    'Bread': 8,
    'Asian': 9,
    'Pasta': 10,
    'Canned Goods': 11,
    'Baking': 12,
    'Cheese': 13,
    'Cereal': 14,
    'Dairy': 15,
    'Drinks': 16,
    'Cleaning': 17,
    'Bathroom': 18,
    'Sweets': 19,

}

def load_ctgs():

    ctgs = {}

    try:

        with open('categories.txt', 'r') as file:

            for line in file:

                if '|' in line:

                    category, priority = line.strip().split('|')
                    ctgs[category.strip()] = int(priority.strip())

            return ctgs
    
    except FileNotFoundError:

        return def_ctgs.copy()


def save_ctgs(ctgs):

    if ctgs is None:

        ctgs is def_ctgs

    with open('categories.txt', 'w') as file:

        for category, priority in ctgs.items():

            file.write(f'{category} | {priority}\n')


def add_category(ctgs):

    for entry, priority in ctgs.items():

        print(f'{priority}. {entry}')
    
    print()
    new_category = input('Enter the name of the new category: ').strip()

    if new_category in ctgs:

        print('Category already exists.')
        return

    while True:

        try:

            new_priority = int(input(
                'Enter an integer where the category is in your shop according to the list above.'
                'Existing priorities will be incremented if neccessary.'
                ).strip())
            
            break

        except ValueError:

            print('Priority must be an integer.')

    
    if new_priority in ctgs.values():

        for key in sorted(ctgs, key=lambda k: ctgs[k], reverse=True):

            if ctgs[key] >= new_priority:

                ctgs[key] += 1

    ctgs[new_category] = new_priority


# Make multiple choice
def delete_category(ctgs):

    pass


# Make drag&drop and/or automatic
def sort_ctgs(ctgs):

    pass


def show_market(ctgs):

    for category, priority in ctgs.items():

        print(f'{priority}. {category}')