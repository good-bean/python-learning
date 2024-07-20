# Write a function that takes a list and returns a string with
# all the items separated by a comma and a space, with 'and'
# inserted before the last item.

def commas(list):
    last = list.pop()
    rtn_string = ""
    for item in list:
        rtn_string += f'{item}, '
    rtn_string += f'and {last}'

    return rtn_string

def main():
    my_list = ['apples', 'bananas', 'tofu', 'cats']
    my_list2 = ['Bridget', 'Mason', 'Samantha', 'Collin', 'Camren', 'Christien']
    print(commas(my_list))
    print(commas(my_list2))

main()