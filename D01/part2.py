def run(list_of_number):
    return [sum(x) for x in (
        [list_of_number[index:index + 3]
         for index in range(len(list_of_number) - 2)
         ])]
