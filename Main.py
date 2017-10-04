import numpy as np
from Functions import *

#Initialize initial tab
#We load and read a csv file
tab

#Example with input lines:
#a b c d
#1 2 3 4

#Call Mapper() function row by row
for row in tab:
    mapper(rowIndex, row)

#Example:
#end of the mapper():
#map(0,[a b c d]) #=> {0:{0,a}},  {1:{0,b}},  {2:{0,c}},  {3:{0,d}}
#map(1,[1 2 3 4]) #=> {0:{1,1}},  {1:{1,2}},  {2:{1,3}},  {3:{1,4}}


#(((
#Shuffle and sort, sort and order by key (here, column index)
#)))

    
#Call Reducer() function key by key
for row in tabMapped:
    reducer(key, row[])
    
#Example:
#end of the reducer()
#{0:   [{0,a}, {1, 1}]} #-> [a 1]
#{1:   [{0,b}, {1, 2}]} #-> [b 2]
#{2:   [{0,c}, {1, 3}]} #-> [c 3]
#{3:   [{0,d}, {1, 4}]} #-> [d 4]

#Example result: inversed tab


