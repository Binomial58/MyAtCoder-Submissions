#include <bits/stdc++.h>
using namespace std;

/* utility : mathematical modulo (always non-negative) */
using ll=long long;
inline int mod(int k, int n)
{
    return (k % n + n) % n;
}

inline long long mod(long long k, long long n)
{
    return (k % n + n) % n;
}

int main() {
    ll a,b;
    cin >> a >> b;
    cout << a*b << endl;
}
