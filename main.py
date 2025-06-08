
 
def count_primes_downwards(n):
    primes = []
    try:
        # 1st provide a list of all numbers from 2 to n
        for i in range(2, n + 1):
            # 2nd check if the number is prime or not
            if is_prime(i):
                primes.append(i)
        return primes
    except:
        return primes


def is_prime(i: int) -> bool:
    try:
        # If the number is less than 2, it is not prime
        if i < 2:
            return False
        # if the number is even, it is not prime
        if i % 2 == 0:
            return False
        # Else True
        else:
            return True
    except:
        return False


def main():
    n = int(input("Enter a number: "))
    print(count_primes_downwards(n))


if __name__ == "__main__":
    main()