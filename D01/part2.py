def run(list_of_number):
    """
    function to linearize a list of data with a system where it sum 3 number to compare only the sums
    199  A
    200  A B
    208  A B C
    210    B C D 607
    200  E   C D 618
    207  E F   D618
    :param list_of_number: (list(int)) List of numbers
    :return: return the list of the sums
    """
    return [sum(x) for x in (
        [list_of_number[index:index + 3]
         for index in range(len(list_of_number) - 2)
         ])]
