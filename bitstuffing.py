def bitStuffing(dataframe: str):
    dataframe = dataframe.replace('11111', '111110')
    flag = '01111110'
    dataframe = flag + dataframe + flag
    return dataframe

def bitDestuffing(dataframe):
    flag = '01111110'
    dataframe = dataframe.replace(flag, '')
    dataframe = dataframe.replace('111110', '11111')
    return dataframe

# Test
dataframe = "010101111110101011100"
print("Original: " + dataframe)
print("Stuffed: " + bitStuffing(dataframe))


print("Destuffed: " + bitDestuffing(bitStuffing(dataframe)))
