def palindrome(num):
    temp =num
    reverse = 0
    while(num>0):
        remainder = num%10
        reverse = (reverse*10)+remainder
        num = num//10
        
    
    if(reverse == temp):
        a=0
    elif(reverse !=temp):
        a=1

    return(a)
        
        
def main():
    T =int(input())
    for i in range(T):
        N = int(input())
        result = palindrome(N)
        print(result)
        
if __name__ == "__main__":
    main()
