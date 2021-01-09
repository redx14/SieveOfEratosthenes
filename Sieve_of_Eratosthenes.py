#Andrey Ilkiv Assignment 6 Problem 1 Section 01

number = int(input("Please Enter a Positive Number"))
maxlength = len(str(number))
while number < 0:
    print("Error")
    number = int(input("Please Enter a Positive Number"))
    maxlength = len(str(number))
    
def SOE(number): 
    count = 0
    spaces = 0
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[n] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for n in range(number + 1)] 
    p = 2
    while (p * p <= number): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True):
              
            # Update all multiples of p 
            for n in range(p * 2, number + 1, p): 
                prime[n] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    # with appropriate spacing for 10 digit max rows
    for p in range(number + 1):
        if count < 10:
            if prime[p]:
                count += 1
                digits = len(str(p))
                spaces = maxlength - digits
                if spaces != 0 :
                    for j in range (spaces):
                        print("  ", end="")
                print (p, end=" ")
        else:
            count = 0
            print("\n", end ="")
  
SOE(number)
