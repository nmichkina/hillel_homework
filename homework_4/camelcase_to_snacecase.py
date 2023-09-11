'''
У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] , перетворити його у список змінних
для Пайтона snace_case, "friends_list", "my_tuple"]
'''

camelcase_list = ["FirstItem", "FriendsList", "MyTuple"]
snakecase_list = []

for camelcase_word in camelcase_list:
    snakecase_list.append("".join(['_'+char.lower()
    if char.isupper()
    else char for char in camelcase_word]).lstrip('_'))
print(snakecase_list)