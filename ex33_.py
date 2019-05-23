def list_append(n_list, test, increment):
    """ Function for appending numbers to the list will the test arrives"""
    i = 0
    print("test is the variable deciding the termination of loop")
    while i < test:
        print(f"Appending i = {i} the list")
        n_list.append(i)
        i = i + increment
    return n_list


if __name__ == "__main__":
    numbers = []
    test = 20
    increment = 5
    # Calling the list_append function
    numbers = list_append(numbers, test, increment)

    for i in range(len(numbers)):
        print(i, end = ' ')
    print("\nThe list numbers is ",numbers)

