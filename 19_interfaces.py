# Question Link:
# https://www.hackerrank.com/challenges/30-interfaces/problem

class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        import math
        result = 0
        i = 1
        while i<= int(math.sqrt(n)) :
            # if 'i' is divisor of 'num'
            if n % i == 0:
                # if both divisors are same then
                # add it only once else add both
                if i == n // i:
                    result = result + i;
                else :
                    result = result + (i + n // i);
            i = i + 1
        return result;


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)