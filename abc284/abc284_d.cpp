#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using u128 = __uint128_t;

/* ---------- gcd ---------- */
ull gcd(ull a, ull b)
{
    while (a)
    {
        b %= a;
        swap(a, b);
    }
    return b;
}

/* ---------- modmul ---------- */
ull modmul(ull a, ull b, ull mod)
{
    return (u128)a * b % mod;
}

/* ---------- modpow ---------- */
ull modpow(ull a, ull e, ull mod)
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

/* ---------- Miller–Rabin ---------- */
bool is_prime(ull n)
{
    if (n < 2)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;

    ull d = n - 1;
    int s = 0;
    while ((d & 1) == 0)
    {
        d >>= 1;
        s++;
    }

    // 64bit deterministic bases
    static ull test_numbers[] = {
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
        for (int r = 1; r < s; r++)
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

/* ---------- Pollard's Rho ---------- */
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

ull find_prime_factor(ull n)
{
    if (n % 2 == 0)
        return 2;
    if (is_prime(n))
        return n;

    while (true)
    {
        ull c = uniform_int_distribution<ull>(1, n - 1)(rng);
        ull x = uniform_int_distribution<ull>(0, n - 1)(rng);
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
            g = gcd((x > y ? x - y : y - x), n);
        }

        if (g != n)
            return g;
    }
}

/* ---------- factorize ---------- */
map<ull, int> factorize(ull n)
{
    map<ull, int> res;
    if (n <= 1)
        return res;

    if (is_prime(n))
    {
        res[n]++;
    }
    else
    {
        ull p = find_prime_factor(n);
        auto l = factorize(p);
        auto r = factorize(n / p);
        for (auto &e : l)
            res[e.first] += e.second;
        for (auto &e : r)
            res[e.first] += e.second;
    }
    return res;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        ll n;
        cin >> n;
        auto f = factorize(n);
        ll ap;
        ll aq;
        for (auto &[p, e] : f)
        {
            if (e == 1)
            {
                aq = p;
            }
            else
            {
                ap = p;
            }
        }
        cout << ap << " " << aq << endl;
    }
}