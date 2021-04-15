def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('zhangsan')


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


name = get_formatted_name('zhang', 'san')
print(name)


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


person = build_person('zhang', 'san')
print(person)


def greet_users(names):
    for user_name in names:
        print("Hello, " + user_name.title() + "!")


names = ['zhangsan', 'lisi', 'wangwu']
greet_users(names)
