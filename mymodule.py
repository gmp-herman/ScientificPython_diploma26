class exercises: 
    """ day 1 exercises """

    def quad_eq(self,a,b,c):        
        
       d = b**2 - 4*a*c
 
       if d >= 0:
          x1 = (-b + d**0.5)/(2*a)
          x2 = (-b - d**0.5)/(2*a)
          return x1, x2
       else: 
          return None, None

    def ex1(self,a,b,c):
        return self.quad_eq(a,b,c)

 
    def rseq(self,n):
        seq = [0]
        i = 1

        while i<n:
           a1 = seq[i-1] - i
          
           if a1 > 0 and a1 not in seq :
                 seq.append(a1)
           else: 
                 seq.append(seq[i-1] + i)
           i = i+1
        return seq

    def ex2(self,n):
        return self.rseq(n)

    def array_sort(self,mylist):
        
        mylist.sort()

        newlist = mylist[::-1]
        
        return newlist

    def ex3(self,mylist):
        return self.array_sort(mylist)

    def list_intersection(self,list1,list2):
        
        list3 = list1 & list2
        
        return list3

    def ex4(self,list1,list2):
        return self.list_intersection(list1,list2)

    def factors(self,m):
        
        t = [(x,y) for x in range(m+1) for y in range(m+1) if x*y==m]
        
        return t

    def ex5(self,m):
        return self.factors(m)

    def palindrome(self,p):
            b = p.upper()
            m = len(b)
            word = []
    
            for i in range(m):
                if b[i] == " ":
                   b.replace(" ","")
                else:
                   word.append(b[i])
    
            reverse = word[::-1]
    
            if word == reverse:
               return print("The word is a palindrome")
            else:
               return print("The word is not a palindrome")
  
    def ex7(self,p):
        return self.palindrome(p)


