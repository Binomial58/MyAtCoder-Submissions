#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)

int main()
{
    ll n, s;
    cin >> n >> s;
    vector<ll> A(n);
    for (auto &x : A)
        cin >> x;
    vector<ll> P(n);
    for (auto &x : P)
        cin >> x;
    ll count = 0;
    for (int a : A)
    {
        for (int p : P)
        {
            if (a + p == s)
            {
                count++;
            }
        }
    }
    cout << count << endl;
}
