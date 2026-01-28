#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)

namespace fastio
{
    // 基本型
    template <class T>
    void wt(const T &x) { cout << x; }

    // 文字列系のオーバーロード
    inline void wt(const char *s) { cout << s; }
    inline void wt(const string &s) { cout << s; }

    // vector 出力（空白区切り）
    template <class T>
    void wt(const vector<T> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << ' ';
            wt(v[i]);
        }
    }

    // 出力本体
    void print() { cout << '\n'; }

    template <class Head, class... Tail>
    void print(const Head &head, const Tail &...tail)
    {
        wt(head);
        if (sizeof...(Tail))
            cout << ' ';
        print(tail...);
    }
} // namespace fastio

using fastio::print;

int main()
{
    ll n, s, sa = 0;
    cin >> n >> s;
    vector<ll> S(2 * n + 1, 0);
    vector<ll> A(n);
    set<ll> SA;
    bool canmake = false;
    for (auto &x : A)
    {
        cin >> x;
        sa += x;
    }
    rep(i, 0, 2 * n)
    {
        S[i + 1] = A[i % n];
    }
    rep(i, 1, 2 * n + 1)
    {
        S[i] += S[i - 1];
    }
    rep(i, 0, 2 * n + 1)
    {
        SA.insert(S[i]);
    }
    s %= sa;
    // print(s);
    // print(S);
    rep(i, 0, n)
    {
        ll a = S[i], t;
        t = s + a;
        // print(t);
        if (SA.count(t))
        {
            canmake = true;
        }
    }
    if (canmake)
    {
        print("Yes");
    }
    else
    {
        print("No");
    }
    // print(SA);
}
