N=int(input('Введите количество слов:'))
st=''
print('Вводите слова')
for i in range(N):
    s=input()
    if i==N-1:
        st=st+s
    else:
        st=st+s+' '
print(st)