import sys

main_menu = ['Display people',
             'Display a person\'s collection',
             'See who has a title',
             'Add a person',
             'Add titles to a person\'s collection',
             'Remove a person',
             'Remove a title',
             'Quit\n']

people = {'Bridget': {'Payal Kadakia': 'LifePass', 'Panos Louridas': 'Algorithms'}}

def display_main():
    print('\nWelcome to the main menu!\n\nKindly make a selection:')
    print('=========================')
    for index, item in enumerate(main_menu):
        print(f'{index + 1}. {item}')

def display_people(people_list):
    print('\nList of people')
    print('=========================')
    for person in people_list.keys():
        print(f' - {person}')
    print()

def display_titles(people_list):
    print('\nType a name to display their collection:')
    name = input()
    for match, match_list in people_list.items():
        if name == match:
            print(f'\n{match}\'s collection:')
            print('=========================')
            for title in match_list:
                print(f'{match_list[title]} by {title}')
            print()

def display_owner(people_list):
    print('\nType a title to see who has it in their collection:')
    title = input()
    for person, title_list in people_list.items():
        if title in title_list.values():
            print(f' - {person}')
        else:
            print('Nobody has that title.\n')
    print()

def add_person(people_list):
    print('\nType the name you want to add:')
    name = input()
    people_list[name] = {}

def add_title(people_list):
    print('\nType the person you want to add the title to:')
    name = input()
    if name not in people_list:
        print(f'\n{name} is not on the list of collections!\n')
        return
    print('\nType the title author:')
    author = input()
    print('\nType the title:')
    title = input()
    for collection, collection_list in people_list.items():
        if name in collection:
            collection_list[author] = title
            print(f'\n{title} by {author} was added to {name}\'s collection.\n')

def get_key(dict, val):
    for name, collection in dict.items():
        for author, title in collection.items():
            if val == title:
                return author

def remove_title(people_list):
    print('\nType the person you want to remove a title from:')
    name = input()
    if name not in people_list.keys():
        print(f'\n{name} is not on the list of collections!\n')
        return
    print('\nWhich title would you like to remove?:')
    title = input()
    key = get_key(people_list, title)
    for name_key, collection in people_list.items():
        if name_key == name:
            try:
                del collection[key]
                print(f'\n{title} has been removed from {name}\'s list of titles!\n')
            except KeyError:
                print('Key not found in collection!')

def remove_person(people_list):
    print('\nType the name of the person you want to remove:')
    name = input()
    if name not in people_list.keys():
        print(f'\n{name} is not on the list of collections!\n')
        return
    del people_list[name]

def main():
    while True:
        menu_choice = 0
        display_main()
        menu_choice = input()
        match menu_choice:
            case '1':
                display_people(people)
            case '2':
                display_titles(people)
            case '3':
                display_owner(people)
            case '4':
                add_person(people)
            case '5':
                add_title(people)
            case '6':
                remove_person(people)
            case '7':
                remove_title(people)
            case '8':
                sys.exit()
            case _:
                break

main()