t=int(input())
def f(T):
    return T**2+2*T+3
print(f(f(f(t)+t)+f(f(t))))