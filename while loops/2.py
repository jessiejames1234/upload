#####################SET A!!!#####################

def grade_list_total(total_list):
    total = 0
    list_count = 0
    i = 0
    while i < len(total_list):
        if total_list[i] >= 50:
            total += total_list[i]

            list_count += 1
        i += 1

    avarage = total / list_count
    return avarage

grade_list1 = [34,65,78,45,54,49,48,50,]
grade_list2 = [34,67,56,45,90,76,23]
print("")
SET_A = grade_list_total(grade_list1)
SET_B = grade_list_total(grade_list2)
print(grade_list1)
print(grade_list2)
print("\nThe average of the passing grades in list1 is:", SET_A)
print("The average of the passing grades in list2 is:", SET_B)


#####################SET B!!!#####################

def grade_list_total(total_list):
    total = 0
    list_count = 0
    i = 0
    while i < len(total_list):
        if total_list[i] < 50:
            total += total_list[i]
            list_count += 1
        i += 1
    avarage = total / list_count
    return avarage

grade_list1 = [34,65,78,45,54,49,48,50,]
grade_list2 = [34,67,56,45,90,76,23]
SET_A = grade_list_total(grade_list1)
SET_B = grade_list_total(grade_list2)
print(grade_list1)
print(grade_list2)
print("\nThe average of the failing grades in list1 is:", SET_A)
print("The average of the failing grades in list2 is:", SET_B)