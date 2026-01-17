#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)

int main() {
    ll n,m;
    cin >> n >> m;
    vector<vector<char>> Ans(n,vector<char>(n,'-'));
    rep(i,0,m){
        ll a,b;
        cin >> a >> b;
        Ans[a-1][b-1]='o';
        Ans[b-1][a-1]='x';
    }
    rep(i,0,n){
        rep(j,0,n){
            cout << Ans[i][j];
            if (j!=n-1){
                cout << " ";
            }
        }
        cout << endl;
    }
}

