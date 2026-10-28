def analyze_numbers(given_list):
    largest = given_list[0]

    for num in given_list:
        if num > largest:
            largest = num

    smallest = given_list[0]
    for num in given_list:
        if num < smallest:
            smallest = num

    sum  = 0
    for num in given_list:
        sum+=num

    avg = sum/len(given_list)

    return largest,smallest,sum,avg


given_list = list(map(int, input("Enter List: ").split()))

largest,smallest,total_sum, average = analyze_numbers(given_list)

print("\nGiven List: ", given_list)
print("\nLargest Number: ", largest)
print("Smallest Number: ", smallest)
print("Sum of all: ", total_sum)
print("Average of Numbers: ", average)