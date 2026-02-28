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
    template <class T, class Container, class Compare>
    void wt(const priority_queue<T, Container, Compare> &q);

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
    template <class T, class Container, class Compare>
    void wt(const priority_queue<T, Container, Compare> &q)
    {
        auto qq = q;
        bool first = true;
        while (!qq.empty())
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(qq.top());
            qq.pop();
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
#define VECI(type, name, size, init) \
    vector<type> name(size, init)
#define VVI(type, name, h, w, init) \
    vector<vector<type>> name(h, vector<type>(w, init))

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

// ===== BEGIN MODINT COPY BLOCK =====
// Copy and paste from this line to the END marker below.
#ifndef MODINT_LIBRARY_MODINT_HPP
#define MODINT_LIBRARY_MODINT_HPP 1

#include <cassert>
#include <type_traits>
#include <utility>

#ifdef _MSC_VER
#include <intrin.h>
#endif

namespace modint_lib
{
    namespace internal
    {

        struct modint_base
        {
        };
        struct static_modint_base : modint_base
        {
        };

        template <class T>
        using is_modint = std::is_base_of<modint_base, T>;
        template <class T>
        using is_modint_t = std::enable_if_t<is_modint<T>::value>;

        template <class T>
        using is_signed_int_t = std::enable_if_t<std::is_integral<T>::value &&
                                                 std::is_signed<T>::value>;

        template <class T>
        using is_unsigned_int_t = std::enable_if_t<std::is_integral<T>::value &&
                                                   std::is_unsigned<T>::value>;

        constexpr long long safe_mod(long long x, long long m)
        {
            x %= m;
            if (x < 0)
                x += m;
            return x;
        }

        constexpr long long pow_mod_constexpr(long long x, long long n, int m)
        {
            if (m == 1)
                return 0;
            unsigned int um = (unsigned int)m;
            unsigned long long r = 1;
            unsigned long long y = (unsigned long long)safe_mod(x, m);
            while (n)
            {
                if (n & 1)
                    r = (r * y) % um;
                y = (y * y) % um;
                n >>= 1;
            }
            return (long long)r;
        }

        constexpr bool is_prime_constexpr(int n)
        {
            if (n <= 1)
                return false;
            if (n == 2 || n == 7 || n == 61)
                return true;
            if ((n & 1) == 0)
                return false;

            long long d = n - 1;
            while ((d & 1) == 0)
                d >>= 1;
            constexpr long long bases[3] = {2, 7, 61};

            for (long long a : bases)
            {
                long long t = d;
                long long y = pow_mod_constexpr(a, t, n);
                while (t != n - 1 && y != 1 && y != n - 1)
                {
                    y = (y * y) % n;
                    t <<= 1;
                }
                if (y != n - 1 && (t & 1) == 0)
                    return false;
            }
            return true;
        }

        template <int n>
        constexpr bool is_prime = is_prime_constexpr(n);

        constexpr std::pair<long long, long long> inv_gcd(long long a, long long b)
        {
            a = safe_mod(a, b);
            if (a == 0)
                return {b, 0};

            long long s = b, t = a;
            long long m0 = 0, m1 = 1;

            while (t)
            {
                long long u = s / t;
                s -= t * u;
                m0 -= m1 * u;
                std::swap(s, t);
                std::swap(m0, m1);
            }

            if (m0 < 0)
                m0 += b / s;
            return {s, m0};
        }

        struct barrett
        {
            unsigned int m_;
            unsigned long long im_;

            explicit barrett(unsigned int m) : m_(m), im_((unsigned long long)(-1) / m + 1) {}

            unsigned int umod() const { return m_; }

            unsigned int mul(unsigned int a, unsigned int b) const
            {
                unsigned long long z = (unsigned long long)a * b;
#ifdef _MSC_VER
                unsigned long long x;
                _umul128(z, im_, &x);
#else
                unsigned long long x = (unsigned long long)(((__uint128_t)z * im_) >> 64);
#endif
                unsigned long long y = x * m_;
                return (unsigned int)(z - y + (z < y ? m_ : 0));
            }
        };

    } // namespace internal

    template <int m, std::enable_if_t<(1 <= m)> * = nullptr>
    struct static_modint : internal::static_modint_base
    {
        using Modint = static_modint;

        static constexpr int mod() { return m; }

        static Modint raw(int v)
        {
            Modint x;
            x.v_ = (unsigned int)v;
            return x;
        }

        static_modint() : v_(0) {}

        template <class T, internal::is_signed_int_t<T> * = nullptr>
        static_modint(T v)
        {
            long long x = (long long)(v % (long long)umod());
            if (x < 0)
                x += umod();
            v_ = (unsigned int)x;
        }

        template <class T, internal::is_unsigned_int_t<T> * = nullptr>
        static_modint(T v)
        {
            v_ = (unsigned int)(v % umod());
        }

        int val() const { return (int)v_; }

        Modint &operator++()
        {
            ++v_;
            if (v_ == umod())
                v_ = 0;
            return *this;
        }

        Modint &operator--()
        {
            if (v_ == 0)
                v_ = umod();
            --v_;
            return *this;
        }

        Modint operator++(int)
        {
            Modint r = *this;
            ++*this;
            return r;
        }

        Modint operator--(int)
        {
            Modint r = *this;
            --*this;
            return r;
        }

        Modint &operator+=(const Modint &rhs)
        {
            v_ += rhs.v_;
            if (v_ >= umod())
                v_ -= umod();
            return *this;
        }

        Modint &operator-=(const Modint &rhs)
        {
            v_ -= rhs.v_;
            if (v_ >= umod())
                v_ += umod();
            return *this;
        }

        Modint &operator*=(const Modint &rhs)
        {
            unsigned long long z = (unsigned long long)v_ * rhs.v_;
            v_ = (unsigned int)(z % umod());
            return *this;
        }

        Modint &operator/=(const Modint &rhs) { return *this *= rhs.inv(); }

        Modint operator+() const { return *this; }
        Modint operator-() const { return Modint() - *this; }

        Modint pow(long long n) const
        {
            assert(0 <= n);
            Modint x = *this, r = 1;
            while (n)
            {
                if (n & 1)
                    r *= x;
                x *= x;
                n >>= 1;
            }
            return r;
        }

        Modint inv() const
        {
            if (prime_)
            {
                assert(v_ != 0);
                return pow((long long)umod() - 2);
            }
            auto eg = internal::inv_gcd((long long)v_, m);
            assert(eg.first == 1);
            return Modint((int)eg.second);
        }

        friend Modint operator+(Modint lhs, const Modint &rhs) { return lhs += rhs; }
        friend Modint operator-(Modint lhs, const Modint &rhs) { return lhs -= rhs; }
        friend Modint operator*(Modint lhs, const Modint &rhs) { return lhs *= rhs; }
        friend Modint operator/(Modint lhs, const Modint &rhs) { return lhs /= rhs; }

        friend bool operator==(const Modint &lhs, const Modint &rhs)
        {
            return lhs.v_ == rhs.v_;
        }

        friend bool operator!=(const Modint &lhs, const Modint &rhs)
        {
            return lhs.v_ != rhs.v_;
        }

    private:
        unsigned int v_;

        static constexpr unsigned int umod() { return (unsigned int)m; }
        static constexpr bool prime_ = internal::is_prime<m>;
    };

    template <int id>
    struct dynamic_modint : internal::modint_base
    {
        using Modint = dynamic_modint;

        static int mod() { return (int)bt_.umod(); }

        static void set_mod(int m)
        {
            assert(1 <= m);
            bt_ = internal::barrett((unsigned int)m);
        }

        static Modint raw(int v)
        {
            Modint x;
            x.v_ = (unsigned int)v;
            return x;
        }

        dynamic_modint() : v_(0) {}

        template <class T, internal::is_signed_int_t<T> * = nullptr>
        dynamic_modint(T v)
        {
            long long x = (long long)(v % (long long)mod());
            if (x < 0)
                x += mod();
            v_ = (unsigned int)x;
        }

        template <class T, internal::is_unsigned_int_t<T> * = nullptr>
        dynamic_modint(T v)
        {
            v_ = (unsigned int)(v % (unsigned int)mod());
        }

        int val() const { return (int)v_; }

        Modint &operator++()
        {
            ++v_;
            if (v_ == umod())
                v_ = 0;
            return *this;
        }

        Modint &operator--()
        {
            if (v_ == 0)
                v_ = umod();
            --v_;
            return *this;
        }

        Modint operator++(int)
        {
            Modint r = *this;
            ++*this;
            return r;
        }

        Modint operator--(int)
        {
            Modint r = *this;
            --*this;
            return r;
        }

        Modint &operator+=(const Modint &rhs)
        {
            v_ += rhs.v_;
            if (v_ >= umod())
                v_ -= umod();
            return *this;
        }

        Modint &operator-=(const Modint &rhs)
        {
            v_ += umod() - rhs.v_;
            if (v_ >= umod())
                v_ -= umod();
            return *this;
        }

        Modint &operator*=(const Modint &rhs)
        {
            v_ = bt_.mul(v_, rhs.v_);
            return *this;
        }

        Modint &operator/=(const Modint &rhs) { return *this *= rhs.inv(); }

        Modint operator+() const { return *this; }
        Modint operator-() const { return Modint() - *this; }

        Modint pow(long long n) const
        {
            assert(0 <= n);
            Modint x = *this, r = 1;
            while (n)
            {
                if (n & 1)
                    r *= x;
                x *= x;
                n >>= 1;
            }
            return r;
        }

        Modint inv() const
        {
            auto eg = internal::inv_gcd((long long)v_, mod());
            assert(eg.first == 1);
            return Modint((int)eg.second);
        }

        friend Modint operator+(Modint lhs, const Modint &rhs) { return lhs += rhs; }
        friend Modint operator-(Modint lhs, const Modint &rhs) { return lhs -= rhs; }
        friend Modint operator*(Modint lhs, const Modint &rhs) { return lhs *= rhs; }
        friend Modint operator/(Modint lhs, const Modint &rhs) { return lhs /= rhs; }

        friend bool operator==(const Modint &lhs, const Modint &rhs)
        {
            return lhs.v_ == rhs.v_;
        }

        friend bool operator!=(const Modint &lhs, const Modint &rhs)
        {
            return lhs.v_ != rhs.v_;
        }

    private:
        unsigned int v_;
        static internal::barrett bt_;

        static unsigned int umod() { return bt_.umod(); }
    };

    template <int id>
    internal::barrett dynamic_modint<id>::bt_(998244353);

    using Modint9 = static_modint<998244353>;
    using Modint1 = static_modint<1000000007>;
    using Modint = dynamic_modint<-1>;

    namespace internal
    {
        template <class T>
        using is_static_modint = std::is_base_of<static_modint_base, T>;
        template <class T>
        using is_static_modint_t = std::enable_if_t<is_static_modint<T>::value>;

        template <class>
        struct is_dynamic_modint : std::false_type
        {
        };
        template <int id>
        struct is_dynamic_modint<dynamic_modint<id>> : std::true_type
        {
        };

        template <class T>
        using is_dynamic_modint_t = std::enable_if_t<is_dynamic_modint<T>::value>;
    } // namespace internal

} // namespace modint_lib

template <int m, std::enable_if_t<(1 <= m)> * = nullptr>
using StaticModint = modint_lib::static_modint<m>;

template <int id>
using DynamicModint = modint_lib::dynamic_modint<id>;

using Modint9 = modint_lib::Modint9;
using Modint1 = modint_lib::Modint1;
using Modint = modint_lib::Modint;

#endif // MODINT_LIBRARY_MODINT_HPP
// ===== END MODINT COPY BLOCK =====

int main()
{
    // Modintを使う
    LL(n, p);
    Modint1 ans = Modint1(p - 1) * Modint1(p - 2).pow(n - 1);
    print(ans.val());
}
