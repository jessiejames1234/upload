def number_list(list):
    i = 0
    sum_all_fail = 0
    count_list_fail = 0
    while i < len(list):
        if list[i] <= 49:
            count_list_fail += 1
            sum_all_fail += list[i]
        i += 1
    average = sum_all_fail / count_list_fail
    return average
grade_list1 = [34,65,78,45,54,49,48,50,]
grade_list2 = [34,67,56,45,90,76,23]
a = number_list(grade_list1)
b = number_list(grade_list2)
print("The average of the failing grades in list1 is:", a)
print("The average of the failing grades in list2 is:", b)