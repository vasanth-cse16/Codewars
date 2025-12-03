def find_average(numbers):
    if len(numbers)==0:
        return 0
    else:
        sum=0
        for i in numbers:
            sum=sum+i
    return sum/len(numbers)
