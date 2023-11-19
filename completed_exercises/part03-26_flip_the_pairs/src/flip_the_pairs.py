number = int(input("Please type in a number: "))
even = 2
odd = 1

if number == 1:
    print(number)

if number > 1: 
    if number % 2 == 0:
        while even <= number:
            print(even)
            even += 2
            while odd <= number:
                print(odd)
                odd += 2
                break
    else:
        while odd <= number:
            if even < number:
                print(even)
                even += 2
            print(odd)
            odd += 2