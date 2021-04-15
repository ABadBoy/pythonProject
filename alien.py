alien_0 = {'color': 'red', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['x_position']
print(alien_0)

user_0 = {
    'name': 'zhangsan',
    'sex': '男'
}
for key, value in user_0.items():
    print("\nkey:" + key)
    print("value:" + value)

for k in user_0.keys():
    print("key:" + k)
