#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, a, b;
    string op;
    cin >> n >> a;
    for (int i = 0; i < n; i++)
    {
        cin >> op >> b;
        if (op == "+")
        {
            a += b;
        }
        else if (op == "-")
        {
            a -= b;
        }
        else if (op == "*")
        {
            a *= b;
        }
        else if (b != 0)
        {
            a /= b;
        }
        else
        {
            cout << "error" << endl;
            break;
        }
        cout << i + 1 << ":" << a << endl;
    }
}