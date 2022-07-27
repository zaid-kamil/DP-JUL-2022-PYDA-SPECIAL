def calculate_da(basic_salary):
    if basic_salary< 10000:
        return basic_salary * 0.15 # 15% da
    elif basic_salary < 25000:
        return basic_salary * 0.175 # 17.5% da 
    else:
        return basic_salary * 0.112 # 11.2% da

def calc_salary(basic_salary, da):
    total = basic_salary + da
    epf = total * .20 # 20% epf
    return total - epf

# usage
bs = int(input("Enter your basic salary: "))
da = calculate_da(bs)
salary = calc_salary(bs, da)
print(f'Your salary is {salary}')