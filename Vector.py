import math 
# This program assigns the class name Vector to a class object.
# The program does several computations using vectors with three co-ordinates
class Vector(object):
    '''   A class used to represent  Vector objects with only an x co-ordinate , y -co-ordinate and z co-ordinate
    Attributes
    ----------
    x : int
         x co-ordinate of the vector
    y : int
         y co-ordinate of the vector
    z : int
         z co-ordinate of the vector
    '''

    def __init__(self, x, y, z):
        ''' when you pass the parameters through the method it returns an instance of the class.'''
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        ''' Returns a string formatted vector based on the components of the vector. '''
        return '(' +str(self.x) +','  + str(self.y) + ','  + str(self.z)+')'

    def add(self,w):
        ''' Passes in  a vector as a parameter and  returns the addition of two vectors .'''
        return(Vector(self.x + w.x , self.y + w.y, self.z + w.z))
    def sub(self,w):
        ''' Passes in a vector as a parameter and  returns the subraction of two vectors.'''
        return(Vector(self.x - w.x , self.y - w.y, self.z - w.z))
    def s_mul(self,s):
        ''' Returns scalar multiplication of a vector by a scalar.'''
        return(Vector(self.x*s , self.y*s, self.z*s))
    def mag(self):
        ''' Returns the magnitude of a vector.'''
        return int(math.sqrt(math.pow(self.x,2) + math.pow(self.y,2) + math.pow(self.z,2) ))
    def dot_prod (self,w):
        ''' Returns the dot product of two vectors .'''
        return self.x * w.x + self.y * w.y + self.z * w.z
    def comp_equal (self,w):
        ''' Returns True if two vectors are identical.'''
        return self.x == w.x and self.y == w.x and self.z == w.z 
    def comp_not_equal (self,w):
        ''' Returns True if two vectors are not identical.'''
        return self.x != w.x or self.y != w.x  or self.z != w.z    


    
V = Vector(2,3,1)
W = Vector(2,4,1)
s = 2
addition = V.add(W)
subtract = V.sub(W)

print(addition)
print(subtract)
print(V.mag())
print(V.s_mul(s))
print(V.dot_prod(W))    
print(V.comp_equal(W))   
print(V.comp_not_equal(W))   

# This program assigns the class name MyComplex to a class object.
# The program does several computations using complex numbers

class MyComplex(object):
    '''   A class used to represent an complex number objects.
    Attributes
    ----------
    real : int
         real component of the vector
    imag : int
         imag component  of the vector
    '''
    def __init__(self, real, imag):
        ''' when you pass the parameters through the method it returns an instance of the class.'''
        self.real = real
        self.imag = imag
        
    def __str__(self):
        ''' Returns a string formatted complex number based on the value of the real and imaginary compoents of the vector '''
        # logic conditions 
        if self.imag > 0 and (self.real <0 or self.real >0 ) :
            return  str(self.real) + "+" + str(self.imag)+'i'
        elif self.imag < 0 and (self.real <0 or self.real >0) :
            return  str(self.real) + str(self.imag)+'i'
        elif self.imag == 0 and (self.real > 0 or self.real < 0):
            return  str(self.real)
        elif self.real == 0 and (self.imag < 0 or self.imag > 0):
            return  str(self.imag) +'i'
        else:
            print('You have entered two zeros in the vector')
            return str(self.real) + "+" + str(self.imag)+'i'
            
    
    def com_mul(self, w):
        ''' Pass a complex number vector as a parameter through the method it returns multiplication with another complex vector.'''
        return MyComplex(self.real*w.real - self.imag*w.imag,
                       self.imag*w.real + self.real*w.imag)

    def com_conj(self):
        ''' Returns multiplication the complex conjugate when applied on an instance .'''
        return MyComplex(self.real,(-1*(self.imag)))
    


V = MyComplex(2,-1)
W = MyComplex(2, 4)
z = V.com_mul(W)
print(z)
c = V.com_conj()
print(c)
