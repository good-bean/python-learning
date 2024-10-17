# An arithmetic arranger function that receives a list of strings which are
# arithmetic problems, and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument. When the second argument is
# set to True, the answers should be displayed.

def arithmetic_arranger(problems, show_answers=False):
    p_dlist = []
    if problem_limiter(problems):
        return "Error: Too many problems."
   
    p_list = [problem.split() for problem in problems]
    for p in p_list:
        p_dlist.append({'left': p[0],
                        'right': p[2],
                        'operator': p[1]})
       
    left = [p['left'] for p in p_dlist]
    right = [p['right'] for p in p_dlist]
    operator = [p['operator'] for p in p_dlist]
   
    if op_check(operator):
        return "Error: Operator must be '+' or '-'."
    if not check_numeric(left) or not check_numeric(right):
        return 'Error: Numbers must only contain digits.'
    if not check_n_len(left) or not check_n_len(right):
        return 'Error: Numbers cannot be more than four digits.'
   
    convert_int(left)
    convert_int(right)
   
    spacing = []
    get_spacing(spacing, left, right)
   
    first_row, second_row, third_row, fourth_row = [], [], [], []
    for i in range(len(left)):
        first_spacing = spacing[i] - len(str(left[i]))
        first_row.append(f'{" " * first_spacing}{left[i]}')
       
        second_spacing = spacing[i] - len(str(right[i])) - 1
        second_row.append(f'{operator[i]}{" " * second_spacing}{right[i]}')
       
        third_row.append(f'{"-" * spacing[i]}')
       
        fourth_answer = ''
        if operator[i] == '+':
            fourth_answer = left[i] + right[i]
        else:
            fourth_answer = left[i] - right[i]
       
        fourth_spacing = spacing[i] - len(str(fourth_answer))
        fourth_row.append(f'{" " * fourth_spacing}{fourth_answer}')
   
    first_row = '    '.join(first_row)
    second_row = '    '.join(second_row)
    third_row = '    '.join(third_row)
    fourth_row = '    '.join(fourth_row)
   
    if show_answers == True:
        return (f'{first_row}\n{second_row}\n{third_row}\n{fourth_row}')
    else:
        return (f'{first_row}\n{second_row}\n{third_row}')

def problem_limiter(problems):
    n_probs = 0
    for _ in problems:
        n_probs += 1
    return n_probs > 5

def op_check(operator):
    for item in operator:
        return (item != '+') and (item != '-')

def check_numeric(n_list):
    for item in n_list:
        # return isinstance(item, int)
        return item.isnumeric()

def check_n_len(n_list):
    for item in n_list:
        return len(str(item)) <= 4

def convert_int(problems):
    for i in range(len(problems)):
        temp = problems[i]
        problems[i] = int(temp)

def get_spacing(spacing, left, right):
    for i in range(len(left)):
        max_len = max(len(str(left[i])), len(str(right[i]))) + 2
        spacing.append(max_len)

print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
