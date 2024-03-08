print('Вводите слова')
st=''
s=input()
while s!='stop':
    st=st+s+' '
    s=input()
st=st[:(len(st)-1)]
print(st)