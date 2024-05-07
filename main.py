"""
Blackjack
"""
# Provide your solution here

def calculate_score(num1:int, num2:int, num3:int):
    num1>=1 and num1 <12
    num2 >= 1 and num2 < 12
    num3 >= 1 and num3 < 12
    sum=num1+num2+num3
    if sum <=21:
        return sum
    elif sum > 21 or sum>21 and num1 == 11 or num2 == 11 or num3 ==11:
        sum=sum-10
        if sum > 21:
            return "BUST"
        else:
            return sum
        return sum

num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
num3=int(input("Enter a third number: "))
sum=calculate_score (num1, num2, num3)
print(sum)

"""
Even Numbers
"""
# Provide your solution here

def even_positive_numbers(my_list):
    new_list = []
    for num in my_list:
        if num <0:
            my_list.remove(num)
        elif num % 2 == 0:
            new_list.append(num)
    return new_list

my_list = [-10, -22, 31, 24, 35, 36]
new_list=even_positive_numbers(my_list)
print(new_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

