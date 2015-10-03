__author__ = 'x1ang.li'

import logging

### switches ###
single_line_of_input = False
trim_items = False
ignore_empty_items = False
sort_output = True
logging_level = logging.INFO
### end of switches ###

def main():
    set_a = set(read_input('list_a'))
    set_b = set(read_input('list_b'))

    # list_a intersect list_b
    intersect = apply_operator(set_a, set_b, lambda a,b: (a & b))
    logging.info('The strings that present in both lists are: %s', intersect)

    # list_a minus list_b
    a_minus_b = apply_operator(set_a, set_b, lambda a,b: (a - b))
    logging.info('The strings that only present in list_a are: %s', a_minus_b)

    # list_a minus list_b
    b_minus_a = apply_operator(set_a, set_b, lambda a,b: (b - a))
    logging.info('The strings that only present in list_b are: %s', b_minus_a)


def apply_operator(set_a, set_b, operator):
    result = operator(set_a, set_b)
    result = sorted(list(result)) if sort_output else result
    return result


def read_input(list_name):

    file_name = list_name + ('_s' if single_line_of_input else '_m') + '.txt'
    logging.info('Opening %s as the input', file_name)

    with open(file_name,'r') as f:
        if (single_line_of_input):
            input_list = f.readline().split()
        else: # multiple lines
            input_list = f.readlines()
            input_list = [s.rstrip('\n\r') for s in input_list]

    if (trim_items):
        input_list = [s.strip() for s in input_list]

    if (ignore_empty_items):
        input_list = filter(None, input_list)

    logging.info('The first ten elements of %s are: %s', list_name, input_list[:10])

    return input_list


if __name__ == "__main__":
    logging.basicConfig(level=logging_level)
    main()