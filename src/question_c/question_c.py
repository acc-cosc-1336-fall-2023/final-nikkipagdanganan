#write functions here, don't add input('') statements here!

# def create_multiplication_table(rows, cols):
#     list0 = []
#     # the list above needs to be populated by 5 lists
#     for i in range(0, rows):
#         row_list = []
#         for j in range(0, cols):
#             row_list.append((i + 1) * (j + 1))
#         list0.append(row_list)
#     print(list0)

# create_multiplication_table(5,10)
    
def create_multiplication_table():
    list0 = []
    for i in range(5):
        row_list = []
        for j in range(10):
            row_list.append((i + 1) * (j + 1))
        list0.append(row_list)
    return list0

def display_multiplication_table():
    list0 = create_multiplication_table()
    for row_list in list0:
        for item in row_list:
            print(str(item).rjust(3, " "), end = " ")

        print(" ")

