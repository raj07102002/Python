# a=(3,2,5,2,2) 

# print(a.count(2)) 

Q.2 def factorial(n): 
    fact=1
    for i in range(1,n+1): 
        if i>0: 
            fact*=i
    print(fact)
x=int(input("Enter any value = "))
factorial(x) 

Q.3 Resturent menu 

print("Welcome to Pythonic Restaurant!")
print("Here is our menu:")
print("1. Burger - ₹80")
print("2. Pizza - ₹150")
print("3. Sandwich - ₹50")
print("4. Coffee - ₹40")
print("5. Exit")

total = 0

while True:
    choice = input("\nEnter the item number you want to order (1-5): ")

    if choice == '1':
        total += 80
        print("Burger added to your order. Total =", total)
    elif choice == '2':
        total += 150
        print("Pizza added to your order. Total =", total)
    elif choice == '3':
        total += 50
        print("Sandwich added to your order. Total =", total)
    elif choice == '4':
        total += 40
        print("Coffee added to your order. Total =", total)
    elif choice == '5':
        print("\nThank you for ordering!")
        print("Your final bill is ₹", total)
        break
    else:
        print("Invalid choice. Please select a valid item number.")

