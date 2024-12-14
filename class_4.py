#x = input("Enter Year:")
#print("Year is: " + x)



#x = 5
#x  += 3
#x -= 3
#x *= 3
#x /= 3
#x %= 3
#x //= 3
#x **= 3
#print(x)


#x=5
#y=10
#
#print (x <= y)#(x==y)

#x = 5
#print (not(x > 3 and x < 10))


#x = input("Enter Year:")
#z = int(x)
#z /= 4
#print(z)


#x = ["apple", "banana"]
#print("banana" in x)

#x = ["apple", "banana"]
#print("pineapple" not in x)

#leap year
#x = input("Enter Year:")
#z = int(x)
#if (z % 4 ==0):
#    print("Leap year")
#elif (z % 4 != 0):
#    print("Not Leap year")


#i=1
#while i<=100:
#    print(i)
#    i +=2
    

#i=2
#while i<10:
#    print(i)
#    i +=2

#i=1
#while i<=10:
#    print(i, "Shazedul")
#    i +=1      


#x = input("Enter first Value:")
#a = int(x)
#y = input("Enter Second Value:")
#b = int(y)  
#z = input("Enter Third Value:")
#c = int(z)
#if (a>b and a>c):
#    print(a)
#elif (b>a and b>c):
#    print(b)
#elif (c>a and c>b):
#    print(c)
#else:
#    print("ALL are Equal")


#x = input("Enter first Value:")
#a = int(x)
#i=1
#while i<a:
#    print(i)
#    i= 6*i - 1


#i = 0
#while i < 100:
#    i +=1
#    if i<3:
#        continue
#    print(1)



num = 2  # Start from 2 since 1 is not a prime number

while num <= 20:  # Loop through numbers from 2 to 20
    i = 2
    while i < num:
        if num % i == 0:  # If divisible, it's not prime
            break
        i += 1
    else:
        print(num)  # Executed only if the inner loop wasn't broken

    num += 1  # Move to the next number