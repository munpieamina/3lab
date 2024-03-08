import random
ko=0
kb=0
while ko<3:
    a=random.randint(1,20)
    b=random.randint(1,20)
    s=str(a)+' + '+str(b)+' = '
    c=int(input(s))
    if a+b==c:
        kb=kb+1
    else:
        ko=ko+1
print('Игра окончена! Правильных ответов:', kb, ':)')