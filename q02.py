print("-" * 30)
print("        員工薪資輸入\n    若姓名處未輸入則代表結束")
print("-" * 30)

employee_list = []
total = 0

while True:
    eName = input("請輸入姓名:")

    if eName == '':
        print("-" * 30)
        break

    eSalary = int(input("請輸入薪資:"))
    print("")

    employee_dict = {'eName': eName, 'eSalary': eSalary}
    employee_list.append(employee_dict)
    total += eSalary

ave = total / len(employee_list) if len(employee_list) > 0 else 0
round(ave)

for employee in employee_list:
    print(f"員工{employee['eName']:<6}的薪資為{employee['eSalary']:>7,}")
print("-" * 30)
print(f"合計薪資 : {total:>15,}")
print(f"平均薪資 : {ave:>18,.2f}")
print("=" * 30)
