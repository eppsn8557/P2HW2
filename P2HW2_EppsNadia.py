# CTI-110
# P2HW2 - List
# Nadia Epps
# 15 October 2023
#
m1grade = float(input('Enter grade for Module 1:'))
m2grade = float(input('Enter grade for Module 2:'))
m3grade = float(input('Enter grade for Module 3:'))
m4grade = float(input('Enter grade for Module 4:'))
m5grade = float(input('Enter grade for Module 5:'))
m6grade = float(input('Enter grade for Module 6:'))
print()
print('------------Results------------')
my_list = [m1grade, m2grade, m3grade, m4grade, m5grade, m6grade]
print(f'Lowest Grade:       {min(my_list)}')
print(f'Highest Grade:      {max(my_list)}')
print(f'Sum of Grades:      {sum(my_list)}')
average = (m1grade + m2grade + m3grade + m4grade + m5grade + m6grade)/6
print(f'Average:            {average:.2f}')
print('----------------------------------------')

