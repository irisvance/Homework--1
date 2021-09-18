print('Enter the current month, day and year: ')

print('Month')
current_month = int(input())
print('\n')

print('Day')
current_day = int(input())
print('\n')

print('Year')
current_year = int(input())
print('\n')

print('Enter your birthday by month, day, and year: ')

print('Month:')
birth_month = int(input())
print('\n')

print('Day:')
birth_day = int(input())
print('\n')

print('Year:')
birth_year = int(input())
print('\n')

user_age = int(current_year - birth_year)
print('You are', user_age, 'years old.')

print('Birthday Calculator\n ')
print('Month: \n', birth_month, '\n')
print('Day: \n', birth_day, '\n')
print('Year: \n', birth_year, '\n')
