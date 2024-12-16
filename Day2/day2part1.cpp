#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <random>
#include <chrono>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <unordered_set>
#include <unordered_map>
#include <sstream>


using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;
const char nl = '\n';

bool isSafe(vector<int>& nums) {
    if (nums.empty()) return false;

    vector<int> sortedNums(nums.begin(), nums.end());
    sort(sortedNums.begin(), sortedNums.end());

    for (int i = 1; i < sortedNums.size(); i++) {
        int diff = abs(sortedNums[i] - sortedNums[i - 1]);
        if (diff < 1 || diff > 3) {
            return false;
        }
    }

    return nums == sortedNums || nums == vector<int>(sortedNums.rbegin(), sortedNums.rend());
}

vector<int> parseLine() {
    vector<int> nums;
    string line;
    getline(cin, line);
    istringstream iss(line);
    int n;
    while (iss >> n) {
        nums.push_back(n);
    }
    return nums;
}
void solve() {
    // g++ -std=c++17 day2part1.cpp -o day2part1 && ./day2part1 < input.txt > output.txt
    int ans = 0;
    for (int i = 0; i < 1000; i++) {
        vector<int> nums = parseLine();
        if(isSafe(nums)) {
            ans += 1;
        }
    }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
