def AND(x,y):
  if x and y == 1:return(1)
  else:return(0)
  

def NOT(x):
  if x == 1:return(0)
  else:return(1)


def OR(x,y):
  if x or y== 1:return(1)
  else:return(0)
  
  
def NAND(x,y):
  return(NOT(AND(x,y)))
  

def XOR(x,y):
  X_=OR(x,y)
  Y_=NAND(x,y)
  return(AND(X_,Y_))

def ADDER(x,y,z):
  #STAGE 1
  XOR1 = XOR(x,y)
  AND1 = AND(x,y)
  #STAGE 2
  AND2 = AND(XOR1,z)
  XOR2 = XOR(XOR1,z)
  #STAGE 3
  OR3 = OR(AND1,AND2)
  return(XOR2,OR3)
  

def NOR(x,y):
  return(NOT(OR(x,y)))
  
  
def BIT4_ADDER(a,b,c,d, a1,b1,c1,d1, s):
  adder1 = ADDER(a,a1,s)
  adder2 = ADDER(b,b1,adder1[1])
  adder3 = ADDER(c,c1,adder2[1])
  adder4 = ADDER(d,d1,adder3[1])
  
  return(adder1[0],adder2[0],adder3[0],adder4[0],adder4[1])
  

def ALU(a,b,c,d, a1,b1,c1,d1, s):
  adder = BIT4_ADDER(a,b,c,d, XOR(a1,s),
                              XOR(b1,s),
                              XOR(c1,s),
                              XOR(d1,s), s)
                              
  #bit_adder = 
  
  n1 = NOT(adder[0])
  n2 = NOT(adder[1])
  n3 = NOT(adder[2])
  n4 = NOT(adder[3])  
  
  and1 = AND(n1,n2)
  and2 = AND(and1,n3)
  and3 = AND(and2,n4)
  
  return({"OUT":[adder[0],adder[1],adder[2],adder[3]],
          "DATA":[adder[4],adder[0],and3]})

x = input("Enter a 4 bit binary number: ")
y = input("Enter another 4 bit binary number: ")
z = input("1 for subtraction and 0 for addation: ")
ALU(int(x[0]),int(x[1]),int(x[2]),int(x[3]), int(y[0]),int(y[1]),int(y[2]),int(y[3]), int(z))
