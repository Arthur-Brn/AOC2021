
def run(list_of_number):
    list_of_number_linear = []
    for index in range(len(list_of_number) - 2):
        list_of_number_linear.append(list_of_number[index] + list_of_number[index + 1] + list_of_number[index + 2])
    print(list_of_number_linear)
    return list_of_number_linear
