hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hrs > 40:
    overrate = rate * 1.5
    overhrs = hrs - 40
# pay = hrs * rate - this would get overwritten by then next line and no errors
pay = (hrs - overhrs) * rate
overpay = overrate * overhrs
gross = overpay + pay
print(gross)