users = {
    'zhangsan': {
        'age': '20',
        'sex': '男'
    },
    'lisi': {
        'age': '20',
        'sex': '男'
    }
}

for user, userInfo in users.items():
    print("\nUserName:" + user + " 年龄是：" + userInfo['age'] + " 性别是：" + userInfo['sex'])
