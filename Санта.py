def santa_users(user_list):
    user_dict = {}

    for user in user_list:
        name = user[0]
        postal_code = user[1] if len(user) > 1 else None
        user_dict[name] = postal_code

    return user_dict


users = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
result = santa_users(users)
print(result)