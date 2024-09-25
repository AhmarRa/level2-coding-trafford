list_of_primes = [2]
 
target_number = int(input("Please enter the maximum number you want to find a list of prime numbers: "))
 
for x in range (3,target_number,2):
    x_is_prime = True
    for y in list_of_primes:
        if x%y == 0:
            x_is_prime = False
    if x_is_prime == True:
        list_of_primes.append(x)
 
# print out prime list
for prime in list_of_primes:
    print(prime)
