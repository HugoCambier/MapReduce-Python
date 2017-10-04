def map(rowIndex,values) :
    #Split the values of the row (because we received a csv)
    #Run the line, column by column
    for(columnIndex = 0 to length(values)) :
        #Column index from 0 to end of row
        K = columnIndex
        V = {rowIndex: values[columnIndex]}
    #Return key + list of values(rowIndex, Value):
    return {K:V}


def shuffleAndSort():
    #Gather elements with the same key and sort them


#Normally, I understood that inversion of rows/columns had to be done
#in the suffleAndSort. I did it in Reducer() to receive good coordinates
#and make the right inversed table.
def reduce(K,V[]) :
    #At the entrance: K,V[] -> {y:{x, val}}
    for(x in V[]) :
        transposedColumnIndex = rowKey(k)
        transposedRowIndex = columnKey
    #At the end: K,V[] -> {x:{y, val}}
    return {transposedRowIndex: {transposedColumnIndex, val}}


