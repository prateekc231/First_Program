def check_col(a,b,c):
    for i in range (3):
        if a[i]==b[i]==c[i]:
            print a[i],'WINNER'
            return 1
def check_row(a,b,c):
    for i in range (1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],'WINNER'
            return 1
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],'WINNER'
            return 1
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],'WINNER'
            return 1
def check_dia(a,b,c):
    for i in range(1):
        if a[0]==b[1]==c[2]:
            print a[0],'WINNER'
            return 1
        elif a[2]==b[1]==c[0]:
            print a[2],'WINNER'
            return 1
def checklast(a,b,c,x):
    d=-1
    if x>0 and x<=9:
        if x==1:
            if a[x-1]==a[x]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
            elif a[x-1]==a[x+1]=='O':
                if a[1]!='O' and a[1]!='X':
                    d=1
            elif a[x-1]==b[x]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            elif a[x-1]==c[x+1]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
            elif a[x-1]==b[x-1]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            elif a[x-1]==c[x-1]=='O':
                if b[0]!='O' and b[1]!='X':
                    d=3
        if x==2:
            if a[x-2]==a[x-1]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
            elif a[x-1]==a[x]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
            elif a[x-1]==b[x-1]=='O':
                if c[1]!='O' and c[1]!='X':
                    d=7
            elif a[x-1]==c[x-1]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
        if x==3:
            if a[x-1]==a[x-2]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
            elif a[x-1]==a[x-3]=='O':
                if a[1]!='O' and a[1]!='X':
                    d=1
            elif a[x-1]==b[x-2]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            elif a[x-1]==c[x-3]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
            elif a[x-1]==b[x-1]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            elif a[x-1]==c[x-1]=='O':
                if b[2]!='O' and b[2]!='X':
                    d=5
        if x==4:
            if a[x-4]==b[x-4]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            if b[x-4]==b[x-3]=='O':
                if b[2]!='O' and b[2]!='X':
                    d=5
            if b[x-4]==b[x-2]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
            if b[x-4]==c[x-4]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
        if x==5:
            if a[x-5]==b[x-4]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            elif a[x-4]==b[x-4]=='O':
                if c[1]!='O' and c[1]!='X':
                    d=7
            elif a[x-3]==b[x-4]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            elif b[x-5]==b[x-4]=='O':
                if b[2]!='O' and b[2]!='X':
                    d=5
            elif b[x-3]==b[x-4]=='O':
                if b[0]!='O' and b[0]!='X':
                    d=3
            elif c[x-5]==b[x-4]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
            elif c[x-3]==b[x-4]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
            elif c[x-4]==b[x-4]=='O':
                if a[1]!='O' and a[1]!='X':
                    d=1
        if x==6:
            if a[x-4]==b[x-4]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            if b[x-4]==b[x-5]=='O':
                if b[0]!='O' and b[0]!='X':
                    d=3
            if b[x-4]==b[x-6]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
            if b[x-4]==c[x-4]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
        if x==7:
            if c[x-7]==c[x-6]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            elif c[x-7]==c[x-5]=='O':
                if c[1]!='O' and c[1]!='X':
                    d=7
            elif c[x-7]==b[x-6]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
            elif c[x-7]==a[x-5]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
            elif c[x-7]==b[x-7]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
            elif c[x-7]==a[x-7]=='O':
                if b[0]!='O' and b[1]!='X':
                    d=3
        if x==8:
            if c[x-8]==c[x-7]=='O':
                if c[2]!='O' and c[2]!='X':
                    d=8
            elif c[x-6]==c[x-7]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            elif c[x-7]==b[x-7]=='O':
                if a[1]!='O' and a[1]!='X':
                    d=1
            elif c[x-7]==a[x-7]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
        if x==9:
            if c[x-7]==c[x-8]=='O':
                if c[0]!='O' and c[0]!='X':
                    d=6
            elif c[x-7]==c[x-9]=='O':
                if c[1]!='O' and c[1]!='X':
                    d=7
            elif c[x-7]==b[x-7]=='O':
                if a[2]!='O' and a[2]!='X':
                    d=2
            elif c[x-7]==a[x-7]=='O':
                if b[2]!='O' and b[2]!='X':
                    d=5
            elif c[x-7]==b[x-8]=='O':
                if a[0]!='O' and a[0]!='X':
                    d=0
            elif c[x-7]==a[x-9]=='O':
                if b[1]!='O' and b[1]!='X':
                    d=4
        if d==-1:
            if a[0]!='O' and a[0]!='X':
                d=0
            elif a[1]!='O' and a[1]!='X':
                d=1
            elif a[2]!='O' and a[2]!='X':
                d=2
            elif b[0]!='O' and b[0]!='X':
                d=3
            elif b[1]!='O' and b[1]!='X':
                d=4
            elif b[2]!='O' and b[2]!='X':
                d=5
            elif c[0]!='O' and c[0]!='X':
                d=6
            elif c[1]!='O' and c[1]!='X':
                d=7
            elif c[2]!='O' and c[2]!='X':
                d=8
    return d
            
