def mostFreqChar(str):


    stats = {} # Empty Dictionary


    for s in str:  #Loop to scan through the given string

        stats[s] = str.count(s)

    max_value = max(stats.values())

    itms = stats.items()

    output = set()

    for key, value in itms:

        if value == max_value: #

            output.add(key)

    return ''.join(output)


str = input("please enter a sentence: ")

print(mostFreqChar(str))