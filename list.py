import categories as ctg
import mainframe as mf

def load_list():

    # List of dictionarys
    # Item, quantity + category, priority
    items = []

    with open('s_list.txt', 'r') as file:

        for line in file:

            if '|' in line:

                item, quantity, category = line.strip().split('|')
                items.append({

                    'item' : item.strip(),
                    'quantity' : int(quantity.strip()),
                    'category' : category.strip()
                    
                })

    return items


def save_list(lst):

    with open('s_list.txt', 'w') as file:

        for entry in lst:

            file.write(f'{entry['item']} | {entry['quantity']} | {entry['category']}\n')


def sort_list(lst):

    pass


def add_item(lst):

    pass


def delete_item(lst):

    pass


def show_list(lst):

    pass