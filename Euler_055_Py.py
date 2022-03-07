#Ariel Tynan
#Euler Problem 055, Lychrel numbers, solved in Python
#Started 7 March 2022

#Reverses integer
def rev_num(n): 
    rev = 0
    while(n > 0):
        temp = n % 10
        rev = rev * 10 + temp
        n = n // 10
    return rev

#Checks if number is palindromic
def pal_Check(n):
    pal = True
    n = str(n) #convert to string for comparison
    for i in range(0,int(len(n))): #len is number of digits in interger
        if n[i] != n[len(n)-1-i]:
            pal = False
            break
    return pal

total = 0 #count of Lychrel numbers
for i in range(1,10000):
    sum = i
    count = 0 #number of reverse adds
    while pal_Check(sum) == False and count < 51: #After 49, number is deemed Lychrel
        sum = sum + rev_num(sum)
        #print(sum)
        count = count + 1
    if count == 51 and pal_Check(sum) == False:
        total = total + 1
        print(i)
print(total)
