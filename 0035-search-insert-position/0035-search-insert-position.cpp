class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n=nums.size()-1, res=0;
        while(res<=n){
            int m=res+(n-res)/2;
            if(nums[m]==target) return m;
            else if(nums[m]<target) res=m+1;
            else n=m-1;
        }
        return res;
    }
};