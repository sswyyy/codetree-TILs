number = input()
numbers = number.split("-")
numbers[1], numbers[2] = numbers[2], numbers[1]
numbers.insert(2,"-")    
numbers.insert(1,"-")
for i in numbers:
    print(i, end = "")