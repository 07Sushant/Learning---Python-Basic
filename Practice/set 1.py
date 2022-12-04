from termcolor import colored
set1 = {1,2,3,4}
set2 = {4,5,6,7}
output1 = set1.union(set2)
output2 = set1.symmetric_difference(set2)
print(output1,"\n",output2)