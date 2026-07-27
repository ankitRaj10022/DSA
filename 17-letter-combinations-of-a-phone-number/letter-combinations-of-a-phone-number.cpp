class Solution {
public:
    vector<string> ans;
    vector<string> mp = {
        "", "", "abc", "def", "ghi",
        "jkl", "mno", "pqrs", "tuv", "wxyz"
    };
    void solve(int index, string &curr, string &digits) {
        if (index == digits.size()) {
            ans.push_back(curr);
            return;
        }
        string letters = mp[digits[index] - '0'];
        for (char ch : letters) {
            curr.push_back(ch);         
            solve(index + 1, curr, digits); 
            curr.pop_back();            
        }
    }

    vector<string> letterCombinations(string digits) {

        if (digits.empty()) return {};
        string curr = "";
        solve(0, curr, digits);
        return ans;
    }
};