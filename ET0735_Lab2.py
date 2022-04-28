def display_main_menu():
    print("display_main_menu")

def get_user_input():
    number = input('Enter some numbers separated by commas: ')
    print(number)
    seperate = number.split(",")
    print(seperate)
    num_float=[]
    for x in seperate:
        num_float.append(float(x))
    print(num_float)
    return num_float

def calc_average_temperature(num=[]):
    total=sum(num)
    num_of_elements=len(num)
    average=total/num_of_elements
    print("The average value " + str(average))

def calc_min_max_temperature(num):
    print("The maximum value is " + str((max(num))))
    print("The minimum value is " + str((min(num))))




def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_float = get_user_input()
    calc_average_temperature(num_float)
    calc_min_max_temperature(num_float)


if __name__ == "__main__":
    main()
