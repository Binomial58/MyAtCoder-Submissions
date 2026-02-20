#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using u32 = uint32_t;
using u64 = uint64_t;

#define rep0(i, n) for (int i = 0; i < (int)(n); ++i)
#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i > (int)(b); --i)
#define srep(i, a, b, step) \
    for (long long i = (a); (step) > 0 ? i < (b) : i > (b); i += (step))

#define all(v) (v).begin(), (v).end()
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))

const int INF = (1 << 30);
const ll INFLL = (1LL << 62);
const ll MOD = 998244353;
const ll MOD2 = 1000000007;

namespace fastio
{
    // 入力
    template <class T>
    void read(T &x) { cin >> x; }

    template <class A, class B>
    void read(pair<A, B> &p)
    {
        read(p.first);
        read(p.second);
    }

    template <size_t I = 0, class... Ts>
    inline enable_if_t<I == sizeof...(Ts)> read_tuple(tuple<Ts...> &) {}
    template <size_t I = 0, class... Ts>
        inline enable_if_t < I<sizeof...(Ts)> read_tuple(tuple<Ts...> &t)
    {
        read(get<I>(t));
        read_tuple<I + 1>(t);
    }
    template <class... Ts>
    void read(tuple<Ts...> &t) { read_tuple(t); }

    template <class T, size_t N>
    void read(array<T, N> &a)
    {
        for (auto &x : a)
            read(x);
    }
    template <class T>
    void read(vector<T> &v)
    {
        for (auto &x : v)
            read(x);
    }
    template <class T>
    void read(deque<T> &v)
    {
        for (auto &x : v)
            read(x);
    }

    template <class Head, class... Tail>
    void read(Head &head, Tail &...tail)
    {
        read(head);
        if constexpr (sizeof...(Tail))
            read(tail...);
    }

    // 基本型
    template <class T>
    void wt(const T &x) { cout << x; }

    // 小数は小数点以下10桁で固定出力
    inline void wt(float x) { cout << fixed << setprecision(10) << x; }
    inline void wt(double x) { cout << fixed << setprecision(10) << x; }
    inline void wt(long double x) { cout << fixed << setprecision(10) << x; }

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

    // forward declarations (two-phase lookup for container elements)
    template <class T>
    void wt(const set<T> &s);
    template <class T>
    void wt(const multiset<T> &s);
    template <class T>
    void wt(const unordered_set<T> &s);
    template <class K, class V>
    void wt(const map<K, V> &m);
    template <class K, class V>
    void wt(const unordered_map<K, V> &m);

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
    void wt(const vector<vector<T>> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << '\n';
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
using fastio::read;

#define INT(...)     \
    int __VA_ARGS__; \
    read(__VA_ARGS__)
#define LL(...)     \
    ll __VA_ARGS__; \
    read(__VA_ARGS__)
#define U32(...)     \
    u32 __VA_ARGS__; \
    read(__VA_ARGS__)
#define U64(...)     \
    u64 __VA_ARGS__; \
    read(__VA_ARGS__)
#define STR(...)        \
    string __VA_ARGS__; \
    read(__VA_ARGS__)
#define CHAR(...)     \
    char __VA_ARGS__; \
    read(__VA_ARGS__)
#define DBL(...)        \
    double __VA_ARGS__; \
    read(__VA_ARGS__)
#define VEC(type, name, size) \
    vector<type> name(size);  \
    read(name)
#define VV(type, name, h, w)                       \
    vector<vector<type>> name(h, vector<type>(w)); \
    read(name)
#define VEC0(type, name, size) \
    vector<type> name(size)
#define VV0(type, name, h, w) \
    vector<vector<type>> name(h, vector<type>(w))

// ordered containers (set/multiset etc.) helpers:
// GE_IT(c, x): iterator to minimum element >= x
// LE_IT(c, x): iterator to maximum element <= x (or end if none)
template <class C, class T>
auto ge_it(const C &c, const T &x)
{
    return c.lower_bound(x);
}

template <class C, class T>
auto le_it(const C &c, const T &x)
{
    auto it = c.upper_bound(x);
    if (it == c.begin())
        return c.end();
    --it;
    return it;
}

template <class C, class T>
typename C::value_type ge_val(const C &c, const T &x)
{
    auto it = ge_it(c, x);
    if (it == c.end())
        throw out_of_range("GE_VAL: no element >= x");
    return *it;
}

template <class C, class T>
typename C::value_type le_val(const C &c, const T &x)
{
    auto it = le_it(c, x);
    if (it == c.end())
        throw out_of_range("LE_VAL: no element <= x");
    return *it;
}

template <class T, class Compare, class Alloc>
bool discard_one(set<T, Compare, Alloc> &s, const T &x)
{
    return s.erase(x) > 0;
}

template <class T, class Compare, class Alloc>
bool discard_one(multiset<T, Compare, Alloc> &s, const T &x)
{
    auto it = s.find(x);
    if (it == s.end())
        return false;
    s.erase(it); // erase only one
    return true;
}

template <class T, class Compare, class Alloc>
int discard_all(set<T, Compare, Alloc> &s, const T &x)
{
    return (int)s.erase(x); // 0 or 1
}

template <class T, class Compare, class Alloc>
int discard_all(multiset<T, Compare, Alloc> &s, const T &x)
{
    return (int)s.erase(x); // remove all x
}

#define GE_IT(c, x) ge_it((c), (x))
#define LE_IT(c, x) le_it((c), (x))
#define GE_VAL(c, x) ge_val((c), (x))
#define LE_VAL(c, x) le_val((c), (x))
#define DISCARD_ONE(c, x) discard_one((c), (x))
#define DISCARD_ALL(c, x) discard_all((c), (x))

// Python-like set operations for std::set:
// A | B, A & B, A - B, A ^ B and in-place variants.
template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator|(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.begin(), a.end(), a.key_comp(), a.get_allocator());
    res.insert(b.begin(), b.end());
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator&(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.key_comp(), a.get_allocator());
    for (const auto &x : a)
    {
        if (b.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator-(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.key_comp(), a.get_allocator());
    for (const auto &x : a)
    {
        if (!b.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator^(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res = a - b;
    for (const auto &x : b)
    {
        if (!a.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator|=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a | b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator&=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a & b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator-=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a - b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator^=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a ^ b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_subset(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    for (const auto &x : a)
    {
        if (!b.contains(x))
            return false;
    }
    return true;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_superset(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    return is_subset(b, a);
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_disjoint(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    for (const auto &x : a)
    {
        if (b.contains(x))
            return false;
    }
    return true;
}

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

long long ipow(long long a, long long e)
{
    long long r = 1;
    while (e > 0)
    {
        if (e & 1)
            r *= a;
        a *= a;
        e >>= 1;
    }
    return r;
}

template <class It>
string join(It first, It last, const string &sep)
{
    ostringstream oss;
    bool first_elem = true;
    for (auto it = first; it != last; ++it)
    {
        if (!first_elem)
            oss << sep;
        first_elem = false;
        oss << *it;
    }
    return oss.str();
}

inline string join(const vector<string> &v, const string &sep)
{
    size_t total = 0;
    if (!v.empty())
        total = (v.size() - 1) * sep.size();
    for (const auto &s : v)
        total += s.size();
    string res;
    res.reserve(total);
    for (size_t i = 0; i < v.size(); ++i)
    {
        if (i)
            res += sep;
        res += v[i];
    }
    return res;
}

inline string join(const string &s, const string &sep)
{
    if (s.empty())
        return "";
    string res;
    if (!sep.empty())
        res.reserve(s.size() + (s.size() - 1) * sep.size());
    for (size_t i = 0; i < s.size(); ++i)
    {
        if (i)
            res += sep;
        res += s[i];
    }
    return res;
}

template <class C>
string join(const C &c, const string &sep)
{
    return join(c.begin(), c.end(), sep);
}

template <class C>
C reversed(C c)
{
    reverse(c.begin(), c.end());
    return c;
}

template <class T>
long long sum(const vector<T> &v)
{
    return accumulate(v.begin(), v.end(), 0LL);
}

struct Graph
{
    int n;
    vector<vector<int>> g;

    Graph(int n = 0) : n(n), g(n) {}

    void add_edge(int u, int v, bool undirected = true)
    {
        g[u].push_back(v);
        if (undirected)
            g[v].push_back(u);
    }

    vector<int> &operator[](int i) { return g[i]; }
    const vector<int> &operator[](int i) const { return g[i]; }
};

namespace pollards_rho
{
    using ull = unsigned long long;
    using u128 = __uint128_t;

    // 最大公約数（ユークリッド）
    inline ull gcd(ull a, ull b)
    {
        while (a)
        {
            b %= a;
            std::swap(a, b);
        }
        return b;
    }

    // a*b mod mod（オーバーフロー回避）
    inline ull modmul(ull a, ull b, ull mod)
    {
        return (u128)a * b % mod;
    }

    // a^e mod mod（二分累乗）
    inline ull modpow(ull a, ull e, ull mod)
    {
        ull r = 1;
        while (e)
        {
            if (e & 1)
                r = modmul(r, a, mod);
            a = modmul(a, a, mod);
            e >>= 1;
        }
        return r;
    }

    // Miller-Rabin（64bit決定版）
    inline bool is_prime(ull n)
    {
        if (n < 2)
            return false;
        if (n == 2)
            return true;
        if ((n & 1) == 0)
            return false;

        ull d = n - 1;
        int s = 0;
        while ((d & 1) == 0)
        {
            d >>= 1;
            ++s;
        }

        static const ull test_numbers[] = {
            2, 3, 5, 7, 11, 13, 17, 19,
            23, 29, 31, 37};

        for (ull a : test_numbers)
        {
            if (a >= n)
                continue;
            ull x = modpow(a, d, n);
            if (x == 1 || x == n - 1)
                continue;
            bool comp = true;
            for (int r = 1; r < s; ++r)
            {
                x = modmul(x, x, n);
                if (x == n - 1)
                {
                    comp = false;
                    break;
                }
            }
            if (comp)
                return false;
        }
        return true;
    }

    // Pollard's Rho で n の非自明因子を1つ返す
    inline ull find_prime_factor(ull n)
    {
        if ((n & 1) == 0)
            return 2;
        if (is_prime(n))
            return n;

        static std::mt19937_64 rng(
            std::chrono::steady_clock::now().time_since_epoch().count());

        while (true)
        {
            std::uniform_int_distribution<ull> dist_c(1, n - 1);
            std::uniform_int_distribution<ull> dist_x(0, n - 1);
            ull c = dist_c(rng);
            ull x = dist_x(rng);
            ull y = x;
            ull g = 1;

            auto f = [&](ull v)
            {
                return (modmul(v, v, n) + c) % n;
            };

            while (g == 1)
            {
                x = f(x);
                y = f(f(y));
                ull diff = (x > y) ? (x - y) : (y - x);
                g = gcd(diff, n);
            }
            if (g != n)
                return g;
        }
    }

    // 素因数分解（n = 1 のときは空）
    inline std::map<ull, int> factorize(ull n)
    {
        std::map<ull, int> res;
        if (n <= 1)
            return res;
        if (is_prime(n))
        {
            res[n]++;
            return res;
        }
        ull p = find_prime_factor(n);
        auto l = factorize(p);
        auto r = factorize(n / p);
        for (auto &e : l)
            res[e.first] += e.second;
        for (auto &e : r)
            res[e.first] += e.second;
        return res;
    }

    // 約数列挙（昇順）
    inline std::vector<ull> divisors(ull n)
    {
        std::vector<ull> res;
        if (n == 0)
            return res;
        auto mp = factorize(n);
        res.push_back(1);
        for (auto &kv : mp)
        {
            ull p = kv.first;
            int e = kv.second;
            std::vector<ull> cur = res;
            ull mul = 1;
            for (int i = 1; i <= e; ++i)
            {
                mul *= p;
                for (ull v : res)
                    cur.push_back(v * mul);
            }
            res.swap(cur);
        }
        std::sort(res.begin(), res.end());
        return res;
    }

} // namespace pollards_rho

int main()
{
    // ここにコードを書く
    LL(n, m);
    VEC(ll, A, n);
    VEC0(bool, Ans, m);
    set<ll> P;
    for (ll a : A)
    {
        auto mp = pollards_rho::factorize(a);
        for (pair<ll, ll> p : mp)
        {
            P.insert(p.first);
        }
    }
    for (ll p : P)
    {
        ll now = p - 1;
        while (now < m)
        {
            if (Ans[now] == 0)
            {
                Ans[now] = 1;
            }
            now += p;
        }
    }
    print(m - sum(Ans));
    rep0(i, m)
    {
        if (Ans[i] == 0)
        {
            print(i + 1);
        }
    }
    // print(Ans);
}
