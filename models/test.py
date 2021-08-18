from collections import Counter
data_list = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,7,7,7,7,7,7,7]
data_list2 = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,7,7,7,7,7,7,7]
least_common = Counter(data_list).most_common()[-1]
most_common = Counter(data_list).values()
# print(least_common)
# print(most_common)

def least(data_list1,data_list2):
    data_total = data_list1 + data_list2
    data_list = data_total.copy()
    counter = 999999999999
    least_common_list = []

    for data in data_total:
        least_common = Counter(data_list).most_common()[-1]
        # print(least_common_list)
        # print(data_list)
        # print(least_common[1])
        if least_common[1] <= counter:
            least_common_list.append(least_common[0])
            counter = least_common[1]
            # mylist = list(filter((r_item).__ne__, mylist))
            # data_list.remove(least_common[0])
            data_list = list(filter((least_common[0]).__ne__,data_list))
    return  least_common_list

test_1 = least(data_list,data_list2)

# print(test_1)

def most(data_list1,data_list2):
    data_total = data_list1 + data_list2
    data_list = data_total.copy()
    counter = 0
    most_common_list = []

    for data in data_total:
        most_common = Counter(data_list).most_common()[0]
        # print(least_common_list)
        # print(data_list)
        # print(most_common[1])
        print(most_common)
        if most_common[1] >= counter:
            most_common_list.append(most_common[0])
            counter = most_common[1]
            # mylist = list(filter((r_item).__ne__, mylist))
            # data_list.remove(least_common[0])
            data_list = list(filter((most_common[0]).__ne__,data_list))
    return  most_common_list

test_2 = most(data_list,data_list2)

print(test_2)