list_of_nums = list(map(int, input("Enter integers separated by spaces: ").split()))
minimum = False
maximum = False

for number in list_of_nums:
    if not (minimum and maximum):
        minimum, maximum = number, number
        
    elif number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number
print(minimum, maximum)
print(maximum - minimum)




