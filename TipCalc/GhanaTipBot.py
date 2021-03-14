meal = float(input("Enter The price of meal/product/service : "))
tip = int(input("Enter The Tip in %: "))
VAT = 0.125

#calculation

tip_amt = meal * VAT/100
vat_amt = meal * VAT
total = meal + tip_amt + vat_amt

print(f"Your Meal was GHS {meal:.2f} and your Tip GHS {tip_amt}")
print(f"your total with VAT was GHS {total:.2f}")