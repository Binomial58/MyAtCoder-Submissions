#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)

int main()
{
    string s;
    cin >> s;
    ll count = 0, len = s.length();
    rep(i, 0, len)
    {
        if (s.at(i) == 'U')
        {
            count += len - 1 - i;
            count += 2 * i;
        }
        else
        {
            count += 2 * (len - 1 - i);
            count += i;
        }
        // cout << count << endl;
    }
    cout << count << endl;
}
