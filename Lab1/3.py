def main():
    # get the number
    N = int(input("Enter N to get the fib numbers up to N:"))
    if N <= 0:
        raise ValueError("N cannot be less than or equal to 0")
    elif N == 1:
        print([0])
    else:
        # for fast runtime, we can allocate the list first with N zeros
        fib = [0] * N
        # set the first index to 1
        fib[1] = 1

        # we iterate from the 2nd index to N, using the previous 2 elements to compute the next fib
        for i in range(2, N):
            fib[i] = fib[i - 1] + fib[i - 2]

        print(fib)


if __name__ == "__main__":
    main()
