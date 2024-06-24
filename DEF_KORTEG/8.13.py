def user(last_nam, ferst_name, **user_info):
    """Строим словарь с инфой о пользователе"""
    user_info['ferst_name'] = ferst_name
    user_info['last_nam'] = last_nam
    return user_info

user_profile = user('Михаил', 'Василевский',
                    location = 'Russ',
                    lives = 'Moscow')


print(user_profile)