
A= 3+2*2
print(A)

A='1234567'
A[1::2]

Name="Michael Jackson"
Name.find('el')

A='1'
B='2'
A+B

tuple1=("A","B","C" )
tuple1[-1]

A=((11,12),[21,22])
A[1]

A=((11,12),[21,22])
A[0][1]

'1,2,3,4'.split(',')

A=[1,'a'] 
B=[2,1,'d']

A * B

V={'A','B'}
V.add('C')

x="Go"

if(x!="Go"):

    print('Stop')

else:

    print('Go ')

print('Mike')

for n in range(3):
    print(n+1)
    

A=['1','2','3']

for a in A:
    print(2*a)
    
    
def Add(x,y):
    z=y+x

    return(y)

Add('1','1') 

class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)

p1=Points(1,2)

p1.print_point()



class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()

with open(example1,"r") as file1