def calories():
    data = open("data.txt", "r")
    maxsum = 0;

    with open('data.txt') as file:
        lines = [line.strip() for line in file]

    elfvalues = [];
    elfsum = 0;
    for item in lines:
        if item == '':
            elfvalues.append(elfsum)
            elfsum = 0;
            continue;
        elfsum = elfsum + int(item)
    # print(elfvalues)
    sortedElves = sorted(elfvalues)
    print(sortedElves)
    maxnum = sortedElves[-1]
    secondnum = sortedElves[-2]
    thirdnum = sortedElves[-3]
    print(maxnum + secondnum + thirdnum)
    return maxnum
    	
    
    # print(lines)
        
    # for line in data:                         
    #     if line in ['\n', '\r\n']:
    #         currentsum = sum(numbers)
    #         if currentsum > maxsum:
    #             maxsum = currentsum
    #             print(numbers)
    #             numbers = [];
                
    #         continue;
    #     numbers.append(int(line))  
    # return maxsum

print(calories())

