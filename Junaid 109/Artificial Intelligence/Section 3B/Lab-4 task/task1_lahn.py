def lahn(cardnumber):   
    lst_digit=cardnumber[-1]
    cardnumber=cardnumber[:-1]
    reverse_num=''
    even_index=[]
    less_by_nine=[]
    sum_num=0
    for i in range(len(cardnumber)):
        x=str(cardnumber[-1])
        reverse_num=reverse_num+x
        cardnumber=cardnumber[:-1]
    for i in range(len(reverse_num)):
        if i%2==0:
            x=int(reverse_num[i])*2
            even_index.append(x)
        else:
            x=int(reverse_num[i])
            even_index.append(x)
    for i in even_index:
        if i>9:
            j=i-9
            less_by_nine.append(j)
        else:
            less_by_nine.append(i)
    for i in less_by_nine:
        sum_num=sum_num + i

    sum_num=sum_num+int(lst_digit)

    if sum_num%10==0:
        return f'valid card'
    else:
        return f'invalid card'

carnumber=int(input("enter your number"))
carnumber=str(carnumber)
if len(carnumber)<16 or  len(carnumber)>16:
    print(f'carde number is not complete')
else:
    print(lahn(carnumber))



