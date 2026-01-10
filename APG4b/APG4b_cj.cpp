#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, ave = 0;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A.at(i);
        ave += A.at(i);
    }
    ave /= n;
    for (int i = 0; i < n; i++)
    {
        cout << abs(ave - A.at(i)) << endl;
    }
}