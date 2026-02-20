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

// debug output (enabled only when LOCAL is defined)
namespace debugio
{
    // 基本型
    template <class T>
    void dwt(const T &x) { cerr << x; }

    inline void dwt(float x) { cerr << fixed << setprecision(10) << x; }
    inline void dwt(double x) { cerr << fixed << setprecision(10) << x; }
    inline void dwt(long double x) { cerr << fixed << setprecision(10) << x; }

    inline void dwt(const char *s) { cerr << s; }
    inline void dwt(const string &s) { cerr << s; }

    template <class A, class B>
    void dwt(const pair<A, B> &p)
    {
        cerr << '(';
        dwt(p.first);
        cerr << ',';
        dwt(p.second);
        cerr << ')';
    }

    template <size_t I = 0, class... Ts>
    inline enable_if_t<I == sizeof...(Ts)> dwt_tuple(const tuple<Ts...> &) {}
    template <size_t I = 0, class... Ts>
        inline enable_if_t < I<sizeof...(Ts)> dwt_tuple(const tuple<Ts...> &t)
    {
        if (I)
            cerr << ',';
        dwt(get<I>(t));
        dwt_tuple<I + 1>(t);
    }
    template <class... Ts>
    void dwt(const tuple<Ts...> &t)
    {
        cerr << '(';
        dwt_tuple(t);
        cerr << ')';
    }

    // forward declarations (two-phase lookup for container elements)
    template <class T>
    void dwt(const set<T> &s);
    template <class T>
    void dwt(const multiset<T> &s);
    template <class T>
    void dwt(const unordered_set<T> &s);
    template <class K, class V>
    void dwt(const map<K, V> &m);
    template <class K, class V>
    void dwt(const unordered_map<K, V> &m);

    // array / vector / deque
    template <class T, size_t N>
    void dwt(const array<T, N> &a)
    {
        cerr << '[';
        for (size_t i = 0; i < N; i++)
        {
            if (i)
                cerr << ',';
            dwt(a[i]);
        }
        cerr << ']';
    }
    template <class T>
    void dwt(const vector<T> &v)
    {
        cerr << '[';
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cerr << ',';
            dwt(v[i]);
        }
        cerr << ']';
    }
    template <class T>
    void dwt(const deque<T> &v)
    {
        cerr << '[';
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cerr << ',';
            dwt(v[i]);
        }
        cerr << ']';
    }

    // set / multiset / unordered_set
    template <class T>
    void dwt(const set<T> &s)
    {
        cerr << '{';
        bool first = true;
        for (const auto &x : s)
        {
            if (!first)
                cerr << ',';
            first = false;
            dwt(x);
        }
        cerr << '}';
    }
    template <class T>
    void dwt(const multiset<T> &s)
    {
        cerr << '{';
        bool first = true;
        for (const auto &x : s)
        {
            if (!first)
                cerr << ',';
            first = false;
            dwt(x);
        }
        cerr << '}';
    }
    template <class T>
    void dwt(const unordered_set<T> &s)
    {
        cerr << '{';
        bool first = true;
        for (const auto &x : s)
        {
            if (!first)
                cerr << ',';
            first = false;
            dwt(x);
        }
        cerr << '}';
    }

    // map / unordered_map
    template <class K, class V>
    void dwt(const map<K, V> &m)
    {
        cerr << '{';
        bool first = true;
        for (const auto &kv : m)
        {
            if (!first)
                cerr << ',';
            first = false;
            dwt(kv.first);
            cerr << ':';
            dwt(kv.second);
        }
        cerr << '}';
    }
    template <class K, class V>
    void dwt(const unordered_map<K, V> &m)
    {
        cerr << '{';
        bool first = true;
        for (const auto &kv : m)
        {
            if (!first)
                cerr << ',';
            first = false;
            dwt(kv.first);
            cerr << ':';
            dwt(kv.second);
        }
        cerr << '}';
    }

    // 出力本体
    void printd() { cerr << '\n'; }

    template <class Head, class... Tail>
    void printd(const Head &head, const Tail &...tail)
    {
        dwt(head);
        if (sizeof...(Tail))
            cerr << ' ';
        printd(tail...);
    }
} // namespace debugio

using fastio::print;
using fastio::read;

#ifdef LOCAL
using debugio::printd;
#else
template <class... Args>
void printd(const Args &...) {}
#endif

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

namespace segtree_lib
{
    namespace internal
    {
        // n 以上の最小の 2 べきを返す
        inline unsigned int bit_ceil(unsigned int n)
        {
            unsigned int x = 1;
            while (x < n)
                x <<= 1;
            return x;
        }

        // 末尾の 0 の個数を返す（n > 0 を想定）
        inline int countr_zero(unsigned int n)
        {
            return __builtin_ctz(n);
        }
    } // namespace internal

#if __cplusplus >= 201703L
    // op: S op(S a, S b)
    // e : S e()
    template <class S, auto op, auto e>
    class segtree
    {
        static_assert(std::is_convertible_v<decltype(op), std::function<S(S, S)>>,
                      "op must work as S(S, S)");
        static_assert(std::is_convertible_v<decltype(e), std::function<S()>>,
                      "e must work as S()");
#else
    // op: S op(S a, S b)
    // e : S e()
    template <class S, S (*op)(S, S), S (*e)()>
    class segtree
    {
#endif
    public:
        // 長さ 0 のセグ木を作る
        segtree() : segtree(0) {}
        // n 要素（すべて e()）で初期化する
        explicit segtree(int n) : segtree(std::vector<S>(n, e())) {}
        // 配列 v からセグ木を構築する
        explicit segtree(const std::vector<S> &v) : n_(static_cast<int>(v.size()))
        {
            size_ = static_cast<int>(internal::bit_ceil(static_cast<unsigned int>(n_)));
            log_ = internal::countr_zero(static_cast<unsigned int>(size_));
            data_.assign(2 * size_, e());
            for (int i = 0; i < n_; ++i)
                data_[size_ + i] = v[i];
            for (int i = size_ - 1; i >= 1; --i)
                update(i);
        }

        // a[p] = x に更新する
        void set(int p, S x)
        {
            assert(0 <= p && p < n_);
            p += size_;
            data_[p] = x;
            for (int i = 1; i <= log_; ++i)
                update(p >> i);
        }

        // a[p] を返す
        S get(int p) const
        {
            assert(0 <= p && p < n_);
            return data_[p + size_];
        }

        // 半開区間 [l, r) の積を返す
        S prod(int l, int r) const
        {
            assert(0 <= l && l <= r && r <= n_);
            S sml = e();
            S smr = e();
            l += size_;
            r += size_;

            while (l < r)
            {
                if (l & 1)
                    sml = op(sml, data_[l++]);
                if (r & 1)
                    smr = op(data_[--r], smr);
                l >>= 1;
                r >>= 1;
            }
            return op(sml, smr);
        }

        // 配列全体の積を返す
        S all_prod() const
        {
            return data_[1];
        }

        // 述語 f を使って max_right を求める（関数ポインタ版）
        template <bool (*f)(S)>
        int max_right(int l) const
        {
            return max_right(l, [](S x)
                             { return f(x); });
        }

        // f(prod(l, r)) が true となる最大の r を返す
        template <class F>
        int max_right(int l, F f) const
        {
            assert(0 <= l && l <= n_);
            assert(f(e()));
            if (l == n_)
                return n_;

            l += size_;
            S sm = e();
            do
            {
                while ((l % 2) == 0)
                    l >>= 1;
                if (!f(op(sm, data_[l])))
                {
                    while (l < size_)
                    {
                        l <<= 1;
                        if (f(op(sm, data_[l])))
                        {
                            sm = op(sm, data_[l]);
                            ++l;
                        }
                    }
                    return l - size_;
                }
                sm = op(sm, data_[l]);
                ++l;
            } while ((l & -l) != l);
            return n_;
        }

        // 述語 f を使って min_left を求める（関数ポインタ版）
        template <bool (*f)(S)>
        int min_left(int r) const
        {
            return min_left(r, [](S x)
                            { return f(x); });
        }

        // f(prod(l, r)) が true となる最小の l を返す
        template <class F>
        int min_left(int r, F f) const
        {
            assert(0 <= r && r <= n_);
            assert(f(e()));
            if (r == 0)
                return 0;

            r += size_;
            S sm = e();
            do
            {
                --r;
                while (r > 1 && (r % 2))
                    r >>= 1;
                if (!f(op(data_[r], sm)))
                {
                    while (r < size_)
                    {
                        r = (r << 1) + 1;
                        if (f(op(data_[r], sm)))
                        {
                            sm = op(data_[r], sm);
                            --r;
                        }
                    }
                    return r + 1 - size_;
                }
                sm = op(data_[r], sm);
            } while ((r & -r) != r);
            return 0;
        }

    private:
        int n_ = 0;
        int size_ = 1;
        int log_ = 0;
        std::vector<S> data_;

        // k 番ノードを子から再計算する
        void update(int k)
        {
            data_[k] = op(data_[2 * k], data_[2 * k + 1]);
        }
    };
} // namespace segtree_lib

ll op(ll a, ll b) { return (a + b); }
ll e() { return 0LL; }

int main()
{
    // ここにコードを書く
    LL(n, q);
    VEC(ll, S, n);
    segtree_lib::segtree<ll, op, e> seg(S);
    ll l, r, x, v;
    rep0(i, q)
    {
        VEC(ll, Q, 3);
        // print(Q[0]);
        if (Q[0] == 1)
        {
            l = Q[1];
            r = Q[2];
            print(seg.prod(l - 1, r));
        }
        else
        {
            x = Q[1];
            v = Q[2];
            seg.set(x - 1, v);
        }
    }
}
