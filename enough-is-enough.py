def delete_nth(order, max_e):
    new_list = []
    for item in order:
        if (new_list.count(item) < max_e):
            new_list.append(item)
    return new_list


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
