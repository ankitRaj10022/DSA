class Solution:
    def fp(self, x,n):
        if n==0: return 1
        a=self.fp(x, n//2)
        if n%2==0: return a*a
        else: return a*a*x

    def myPow(self, x: float, n: int) -> float:
       ## return x**n
       if n>=0: return self.fp(x,n)
       else: return 1/self.fp(x, n*(-1))

