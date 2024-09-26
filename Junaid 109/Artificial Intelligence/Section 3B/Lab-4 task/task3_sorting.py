def sort(userinput):
    value=userinput.split(' ')
    ascii=[]
    sorting_text=''
    for i in value:
        ascii.append([ord(i[0]),i])

    for i in range(len(ascii)-1):
        lower_ascii,value=ascii[i]
    
        for h in range(1+i,len(ascii)):
            if ascii[i][0]>ascii[h][0]: 
                lower_ascii,value=ascii[h] 
                ascii[h]=ascii[i] 
                ascii[i]=lower_ascii,value
    
    for i in ascii:
        _,text=i
        sorting_text=sorting_text + text+' '

    return sorting_text

userinput=input('write something')       
print(sort(userinput))