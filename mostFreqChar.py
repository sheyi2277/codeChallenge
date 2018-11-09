def mostFreqChar(str):


    stats = {} # Empty Dictionary


    for s in str:

        stats[s] = str.count(s)

    max_value = max(stats.values())

    itms = stats.items()

    output = set()

    for key, value in itms:

        if value == max_value: #check if the charater in the list is the most frequent

            output.add(key) #if there are more than one most frequent character add to the list

    return ''.join(output) #return most frequent character


str = input("please enter a sentence: ")

print(mostFreqChar(str)) #function call and output

