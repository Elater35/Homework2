# 1. Квадрат числа.

number_1 = int(input("Enter the integer number: "))

square_of_number_1 = number_1 ** 2
print("Square of the number = ", square_of_number_1, end=" \n \n")

# 2. Середнє арифметичне трьох чисел.

number_2 = int(input("Enter the integer number 1: "))
number_3 = int(input("Enter the integer number 2: "))
number_4 = int(input("Enter the integer number 3: "))

arithmetic_mean_of_three_numbers = (number_2 + number_3 + number_4) / 3
print("Arithmetic mean of this numbers = ", arithmetic_mean_of_three_numbers, end=" \n \n")

# 3. Перетворення хвилин у години.

number_minutes = int(input("Enter the number of minutes: "))

convert_minutes_to_hours = number_minutes // 60
convert_minutes_to_remainder_minutes = number_minutes % 60
print("Convert minutes to hours and minutes= ", convert_minutes_to_hours, "hours", convert_minutes_to_remainder_minutes, "minutes", end=" \n \n")

# 4. Розрахунок знижки на вартість товару.

price_of_product = int(input("Enter the price of product: "))
discount_on_the_price = int(input("Enter the discount on the cost of the product in percentage: "))

value_of_discount = price_of_product * discount_on_the_price / 100
cost_after_discount = price_of_product - value_of_discount

print("Cost after discount = ", cost_after_discount, end=" \n \n")

# 5. Остання цифра числа.

number_5 = int(input("Enter any integer number: "))

last_digit_of_number = number_5 % 10

print("Last digit of the number = ", last_digit_of_number, end=" \n \n")

# 6. Периметр прямокутника.

length_of_rectangle = int(input("Enter the length of the rectangle: "))
width_of_rectangle = int(input("Enter the width of the rectangle: "))

perimeter_of_rectangle = (length_of_rectangle + width_of_rectangle) * 2
print("Perimeter of the rectangle = ", perimeter_of_rectangle, end=" \n \n")

# 7. Виведення числа в стовпчик.

number_6 = int(input("Enter any four-digit integer: "))

thousandth_digit = number_6 // 1000
rest_without_thousand = number_6 % 1000

hundredth_digit = rest_without_thousand // 100
rest_without_hundred = rest_without_thousand % 100

tenth_digit = rest_without_hundred // 10
single_digit = rest_without_hundred % 10

print(thousandth_digit)
print(hundredth_digit)
print(tenth_digit)
print(single_digit)
