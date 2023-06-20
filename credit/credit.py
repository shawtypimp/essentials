def categorize_members(members):
    category_list = []
    for member in members:
        age, handicap = member[0], member[1]
        if age >= 55 and handicap > 7:
            category_list.append("Senior")
        else:
            category_list.append("Open")
    return category_list


# Пример участников
potential_members = [(60, 10), (50, 8), (65, 12), (45, 6)]
result = categorize_members(potential_members)
print(result)
