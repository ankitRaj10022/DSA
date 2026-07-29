class Solution {
public:
    const long long LIMIT = 1000000LL + 5;
    vector<long long> fact;
    long long countWays(vector<int>& cnt) {
        int total = 0;
        for (int x : cnt) total += x;
        long double res = 1.0;
        int rem = total;
        for (int c : cnt) {
            if (c == 0) continue;
            for (int i = 1; i <= c; i++) {
                res *= (rem - c + i);
                res /= i;
                if (res > LIMIT) return LIMIT;
            }
            rem -= c;
        }
        return min((long long)(res + 0.5), LIMIT);
    }

    string smallestPalindrome(string s, int k) {
        vector<int> freq(26);
        for (char c : s) freq[c - 'a']++;
        vector<int> half(26);
        string mid = "";
        int halfLen = 0;
        for (int i = 0; i < 26; i++) {
            half[i] = freq[i] / 2;
            halfLen += half[i];
            if (freq[i] & 1)mid.push_back(char('a' + i));
        }

        if (countWays(half) < k)return "";
        string left;
        for (int pos = 0; pos < halfLen; pos++) {
            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                long long ways = countWays(half);
                if (ways >= k) {
                    left.push_back(char('a' + c));
                    break;
                }
                k -= ways;
                half[c]++;
            }
        }

        string right = left;
        reverse(right.begin(), right.end());
        return left + mid + right;
    }
};