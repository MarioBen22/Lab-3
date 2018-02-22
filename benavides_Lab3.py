# Mario Benavides
# Program Status - completed
# this program shows the dollar and total amount of the package after discount.

#get the purchased amount from the user.
total_packages = int(input('Enter the number of packages purchased: '))

# named percentage discounts for the number of packages.
package_cost = 99
quantity1_9 = 0
quantity10_19 = .10
quantity20_49 = .20
quantity50_99 = .30
quantity100_more = .40

# calculations to be used as needed.
normal_cost = (package_cost * total_packages)

discount_total10 = ((package_cost * total_packages) * quantity10_19) 
discount_total20 = ((package_cost * total_packages) * quantity20_49)
discount_total30 = ((package_cost * total_packages) * quantity50_99)
discount_total40 = ((package_cost * total_packages) * quantity100_more)

discounted_total10 = ((package_cost * total_packages) - discount_total10)
discounted_total20 = ((package_cost * total_packages) - discount_total20)
discounted_total30 = ((package_cost * total_packages) - discount_total30)
discounted_total40 = ((package_cost * total_packages) - discount_total40)

# discount thresholds.
if total_packages >= 10:
    if total_packages >=10 and total_packages <=19:
        print('Discount Amount: $', format(discount_total10, ',.2f'))
        print('Total Amount: $', format(discounted_total10, ',.2f'))
    
    if total_packages >= 20 and total_packages <= 49:
        print('Discount Amount: $', format(discount_total20, ',.2f'))
        print('Total Amount: $', format(discounted_total20, ',.2f'))
        
    if total_packages >= 50 and total_packages <= 99:
        print('Discount Amount: $', format(discount_total30, ',.2f'))
        print('Total Amount: $', format(discounted_total30, ',.2f'))
        
    if total_packages >= 100: 
        print('Discount Amount: $', format(discount_total40, ',.2f'))
        print('Total Amount: $', format(discounted_total40, ',.2f'))
        

else:
    print('Discount Amount: $ 00.00 ')
    print('Total Amount: $', format(normal_cost, ',.2f'))
    
