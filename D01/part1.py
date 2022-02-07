def run(list_of_number):
    return sum([1 if x[0] < x[1] else 0
                for x in (
                    [list_of_number[index:index + 2]
                     for index in (range(len(list_of_number) - 1))]
                )]
               )

