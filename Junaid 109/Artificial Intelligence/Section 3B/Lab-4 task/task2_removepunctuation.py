def  punctuation_remover(userinput):
    punctuations='''.,?!:;'"()#[]}{-—.../\*&@_~^|'''
    string_without_punctuation=''
    for i in userinput:
        if i in punctuations:
            continue
        else:
            string_without_punctuation+=i
    return  string_without_punctuation

userinput=input('write your sentence')

print(punctuation_remover(userinput))