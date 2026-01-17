#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        ll a, b, c;
        cin >> a >> b >> c;
        // ll na = a, nb = b, nc = c;
        cout << min(min(a, c), (a + b + c) / 3) << endl;
    }
}
