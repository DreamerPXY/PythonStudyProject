'''求两个数的最大公约数'''
def gcd(x, y):
    (x,y) = (y,x) if x>y else (x,y)
    for i in range(x,(x//2)-1,-1):
        '''从大到小找到两个数都能除得尽的数'''
        if x % i == 0 and y % i == 0:
            return i

'''求两个数的最小公倍数'''
def lcm(x,y):
    return x * y // gcd(x,y)

"""判断一个数是不是回文数"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

print(gcd(3,7))
print(lcm(3,7))
print(is_palindrome(33033))
