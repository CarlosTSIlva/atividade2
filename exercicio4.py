def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(1, 101):
        if is_prime(i):
            print(f"{i} é numero primo.")
        else:
            print(f"{i} não é numero primo.")