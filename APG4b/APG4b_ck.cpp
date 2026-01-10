#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    int l, now;
    now = 1;
    cin >> s;
    l = (s.size() - 1) / 2;
    for (int i = 0; i < l; i++)
    {
        if (s.at(1 + 2 * i) == '+')
        {
            now++;
        }
        else
        {
            now--;
        }
    }
    cout << now << endl;
}