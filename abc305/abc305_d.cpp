#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep0(i, n) for (int i = 0; i < (int)(n); ++i)
#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)

namespace fastio
{
    // 基本型
    template <class T>
    void wt(const T &x) { cout << x; }

    // 文字列系
    inline void wt(const char *s) { cout << s; }
    inline void wt(const string &s) { cout << s; }

    // pair
    template <class A, class B>
    void wt(const pair<A, B> &p)
    {
        wt(p.first);
        cout << ' ';
        wt(p.second);
    }

    // tuple
    template <size_t I = 0, class... Ts>
    inline enable_if_t<I == sizeof...(Ts)> wt_tuple(const tuple<Ts...> &) {}
    template <size_t I = 0, class... Ts>
        inline enable_if_t < I<sizeof...(Ts)> wt_tuple(const tuple<Ts...> &t)
    {
        if (I)
            cout << ' ';
        wt(get<I>(t));
        wt_tuple<I + 1>(t);
    }
    template <class... Ts>
    void wt(const tuple<Ts...> &t) { wt_tuple(t); }

    // array / vector / deque
    template <class T, size_t N>
    void wt(const array<T, N> &a)
    {
        for (size_t i = 0; i < N; i++)
        {
            if (i)
                cout << ' ';
            wt(a[i]);
        }
    }
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
    template <class T>
    void wt(const deque<T> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << ' ';
            wt(v[i]);
        }
    }

    // set / multiset / unordered_set
    template <class T>
    void wt(const set<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }
    template <class T>
    void wt(const multiset<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }
    template <class T>
    void wt(const unordered_set<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }

    // map / unordered_map
    template <class K, class V>
    void wt(const map<K, V> &m)
    {
        bool first = true;
        for (auto &kv : m)
        {
            if (!first)
                cout << " | ";
            first = false;
            wt(kv.first);
            cout << ':';
            wt(kv.second);
        }
    }
    template <class K, class V>
    void wt(const unordered_map<K, V> &m)
    {
        bool first = true;
        for (auto &kv : m)
        {
            if (!first)
                cout << " | ";
            first = false;
            wt(kv.first);
            cout << ':';
            wt(kv.second);
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

template <class T>
int bisect_left(const vector<T> &v, const T &x)
{
    return int(lower_bound(v.begin(), v.end(), x) - v.begin());
}

template <class T>
int bisect_right(const vector<T> &v, const T &x)
{
    return int(upper_bound(v.begin(), v.end(), x) - v.begin());
}

int main()
{
    // ここにコードを書く
    ll n, q;
    cin >> n;
    vector<ll> A(n);
    for (auto &x : A)
        cin >> x;
    vector<ll> Sa(n);
    rep(i, 1, n)
    {
        Sa[i] = Sa[i - 1];
        if (i % 2 == 0)
        {
            Sa[i] += A[i] - A[i - 1];
        }
    }
    // print(A);
    // print(Sa);
    cin >> q;
    ll l, r;
    rep0(i, q)
    {
        cin >> l >> r;
        ll li = bisect_left(A, l), ri = bisect_left(A, r), tl = Sa[li], tr = Sa[ri];
        // print(li, ri);
        // print(tl, tr);
        if (li % 2 == 0)
        {
            tl -= A[li] - l;
        }
        if (ri % 2 == 0)
        {
            tr -= A[ri] - r;
        }
        print(tr - tl);
    }
}
