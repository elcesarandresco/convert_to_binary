def binary_converter(num) -> int:
    
    new_num = num
    list_nums = []
    binary_num = []
    
    while new_num != 0:
        list_nums.append(new_num)
        division = new_num // 2
        new_num = division

    for i in list_nums:
        operation = i % 2
        binary_num.append(str(operation))

    binary_num = "".join(binary_num)

    print(binary_num)


def run():
    num = int(input("Insert a number to convert in binary: "))
    binary_converter(num)


if __name__ == "__main__":
    run()
