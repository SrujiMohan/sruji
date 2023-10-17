work_hours = [("ram", 45), ("ben", 33), ("rama", 56)]

def employee_check(work_hours):
    currentmax = 0
    empofthemonth= " "

    for name,hours in work_hours:
        if hours > currentmax:
            currentmax=hours
            empofthemonth=name
        else:
            pass
    return(empofthemonth,currentmax)

result = (employee_check(work_hours))
print(result)
