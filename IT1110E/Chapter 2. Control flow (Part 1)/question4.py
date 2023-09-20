basic_salary = int(input())

gross_salary = 0

if basic_salary <= 10000:
    da = basic_salary * (80/100)
    hra = basic_salary * (20/100)
    gross_salary = basic_salary + da + hra
elif 10001 <= basic_salary <= 20000:
    da = basic_salary * (90/100)
    hra = basic_salary * (25/100)
    gross_salary = basic_salary + da + hra
elif basic_salary >= 20001:
    da = basic_salary * (95/100)
    hra = basic_salary * (30/100)
    gross_salary = basic_salary + da + hra  

print('%.2f' % gross_salary)