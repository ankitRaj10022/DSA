class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> freq(26);
        for(char c: s) freq[c-'a']++;

        string l, mid;

        for(int i=0; i<26; i++){
            l.append(freq[i] / 2, 'a' + i);
            if(freq[i]%2) mid = char('a' + i);
        }
        
        string r=l;
        reverse(r.begin(), r.end());

        return l+mid+r;
    }
};