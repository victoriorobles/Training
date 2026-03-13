def countResponseTimeRegressions(responseTimes):
    # Write your code here
    size =len(responseTimes)
    counter = 0
    ave = 0
    if 0 == size or 1 == size:
        return counter
    else:
        for i in range(1,size):
            ave = sum(responseTimes[:i])/i
            counter = counter + 1 if responseTimes[i] > ave else counter
    return counter

response = [100, 200, 150,300]

print(countResponseTimeRegressions(response))