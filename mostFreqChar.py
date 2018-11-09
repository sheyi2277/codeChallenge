import os
import psutil

process = psutil.Process(os.getpid())
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

print("the most frequents character(s) : " +mostFreqChar(str)) #function call and output
print("The memory consumption is: " )
print(process.memory_info().rss)


