from functions2 import *
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
print a,'\n',b,'\n',c
j=2
p=0
pr=100
print '\nComputers Chance\n'
b[1]='X'
print a,'\n',b,'\n',c
while j<=9:
    if j%2!=0:
        print '\nComputers Chance\n'
        q= checklast(a,b,c,pr)
        #print q,'\n'
        if q<0:
            c[1]='X'
        if q>=0 and q<3:
            a[q]='X';
        elif q>=3 and q<6:
            b[q-3]='X'
        elif q>=6:
            c[q-6]='X'
        #print a,'\n',b,'\n',c
    elif j%2==0:
         x=input('Player 2 Enter location :-')
         if x<=3:
             if a[x-1]=='X' or a[x-1]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 a[x-4]='O'
         if x>3 and x<=6:
             if b[x-4]=='X' or b[x-4]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 b[x-4]='O'
         if x>6 and x<=9:
             if c[x-7]=='X' or c[x-7]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 c[x-7]='O'
         if x<=0 or x>9:
             print 'Enter valid location'
             j=j-1
         pr=x
    j=j+1
    print a,'\n',b,'\n',c
    if check_col(a,b,c) or check_row(a,b,c) or check_dia(a,b,c):
        p=1
        break

if p==0:
    print 'Match Draw'
rathore=input('last')
