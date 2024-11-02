def try_number(number_list):
    i = 0
    sum = 0
    while i < len(number_list):
        if number_list[i] % 2 != 0:
            sum += number_list[i]
        i += 1
    print("TRY!", sum)
number_list = [1,4,5,6,8,10,11,12]
try_number(number_list)






