#!/usr/bin/env python
# coding: utf-8

# In[1]:


def product_or_sum(a, b):
    product = a * b
    if product > 1000:
        return a + b
    else:
        return product

print(product_or_sum(20, 30))
print(product_or_sum(50, 30)) 


# In[2]:


def print_sum_with_previous():
    previous_num = 0
    print("Current Number  Previous Number  Sum")
    
    for current_num in range(10):
        total = current_num + previous_num
        print(f"{current_num:<15} {previous_num:<17} {total}")
        previous_num = current_num 

print_sum_with_previous()


# In[3]:


def print_even_index_characters(input_str):
    print("Characters at even index positions:")
    for index in range(0, len(input_str), 2):
        print(input_str[index])

input_string = "Krupali"
print_even_index_characters(input_string)


# In[4]:


def check_first_last(nums):
    if not nums: 
        return False
    return nums[0] == nums[-1]

print(check_first_last([1, 2, 3, 1]))  
print(check_first_last([5, 6, 7]))     
print(check_first_last([]))             


# In[5]:


def combine_odd_even(list1, list2):
    odd_elements = list1[1::2]
    even_elements = list2[0::2]
    combined_list = odd_elements + even_elements
    
    return combined_list

list1 = [10, 20, 30, 40, 50, 60]
list2 = [7, 8, 9, 10, 11, 12]

result = combine_odd_even(list1, list2)
print(result)  


# In[6]:


def modify_list(input_list):
    
    elem = input_list.pop(4)
    
    input_list.insert(2, elem)
    
    input_list.append(elem)
    
    return input_list

my_list = [10, 20, 30, 40, 50, 60, 70]
result = modify_list(my_list)
print(result)


# In[7]:


def slice_and_reverse(lst):
    chunk_size = len(lst) // 3
    
    chunk1 = lst[0:chunk_size]
    chunk2 = lst[chunk_size:2*chunk_size]
    chunk3 = lst[2*chunk_size:3*chunk_size]
    
    chunk1.reverse()
    chunk2.reverse()
    chunk3.reverse()
    
    return [chunk1, chunk2, chunk3]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = slice_and_reverse(my_list)
print(result)


# In[8]:


def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_occurrences(my_list)
print(result)


# In[9]:


color_set = {'yellow', 'orange'}
color_list = ['blue', 'black']

color_set.update(color_list)

print(color_set)


# In[10]:


def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  

print_pattern(5)


# In[11]:


def sum_upto_n(n):
    return sum(range(1, n + 1))

num = 10
result = sum_upto_n(num)
print(f"Sum of numbers from 1 to {num} is {result}")


# In[12]:


def display_divisible_by_5(nums):
    for num in nums:
        if num > 150:
            break
        if num % 5 == 0:
            print(num)

my_list = [10, 25, 37, 50, 120, 155, 60, 75]
display_divisible_by_5(my_list)


# In[13]:


def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

my_list = [1, 2, 3, 4, 5]
result = reverse_list(my_list)
print(result)


# In[14]:


List1 = [10, 20, 30, 40]
reversed_list = []

for i in range(len(List1) - 1, -1, -1):
    reversed_list.append(List1[i])

print(reversed_list)


# In[15]:


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=' ')
    print()

display_primes(10, 50)


# In[16]:


class Car:
    def __init__(self, brand, model, price, color, year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.year = year

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")

    def __str__(self):
        return f"{self.brand} {self.model} (${self.price})"

class Showroom:
    def __init__(self):
        self.cars = []

    def view_cars(self):
        if not self.cars:
            print("No cars available in the showroom.")
            return
        print("Currently available cars:")
        for idx, car in enumerate(self.cars, start=1):
            print(f"{idx}. {car}")

    def display_car_details(self, brand, model):
        for car in self.cars:
            if car.brand.lower() == brand.lower() and car.model.lower() == model.lower():
                print("Car details:")
                car.display_details()
                return
        print(f"No car found with brand '{brand}' and model '{model}'.")

    def sell_car(self, brand, model):
        for i, car in enumerate(self.cars):
            if car.brand.lower() == brand.lower() and car.model.lower() == model.lower():
                sold_car = self.cars.pop(i)
                print(f"Sold car: {sold_car}")
                return
        print(f"Car {brand} {model} is not available to sell.")

    def buy_car(self, brand, model, price, color, year):
        new_car = Car(brand, model, price, color, year)
        self.cars.append(new_car)
        print(f"Bought car: {new_car}")

if __name__ == "__main__":
    showroom = Showroom()

    showroom.buy_car("Toyota", "Camry", 25000, "Red", 2020)
    showroom.buy_car("Honda", "Civic", 22000, "Blue", 2019)
    showroom.buy_car("Tesla", "Model 3", 45000, "White", 2021)

    showroom.view_cars()
    print()

    showroom.display_car_details("Honda", "Civic")
    print()

    showroom.sell_car("Toyota", "Camry")
    print()

    showroom.view_cars()
    print()

    showroom.buy_car("BMW", "X5", 60000, "Black", 2022)
    print()

    showroom.view_cars()


# In[ ]:




