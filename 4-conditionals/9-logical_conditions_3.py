Without running the following code,
determine what will be printed.

sale = True
admission_price = (5.25 if not sale else 3.99)

expression1    if    condition      expression2
5.25           if    not sale       3.99
                    sale=True => not sale=False
                    False leads to
print(f"${admission_price}")
