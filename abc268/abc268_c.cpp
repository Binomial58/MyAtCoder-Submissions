#include <bits/stdc++.h>
using namespace std;
int mod(int k, int n)
{
    if (k >= 0)
    {
        return k % n;
    }
    else
    {
        return (n + k) % n;
    }
}
int main()
{
    int n;
    cin >> n;
    vector<int> P(n);
    for (int i = 0; i < n; i++)
    {
        cin >> P.at(i);
    }
    // 配列の確認
    // for (int i = 0; i < n; i++)
    // {
    //     cout << P.at(i) << " ";
    // }
    vector<int> Q(n, 0);
    for (int i = 0; i < n; i++)
    {
        int p = P.at(i);
        for (int j = -1; j < 2; j++)
        {
            Q.at(mod(i - (p + j), n)) += 1;
            // cout << p << mod(p + j, n) << endl;
        }
        // for (int i = 0; i < n; i++)
        // {
        //     cout << Q.at(i) << " ";
        // }
        // cout << endl;
    }
    int maxp = 0;
    for (int x : Q)
    {
        maxp = max(maxp, x);
    }
    cout << maxp << endl;
}
