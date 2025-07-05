class Solution {
    public boolean canJump(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];

        if (nums.length <= 1) return true;
        if (nums[0] == 0) return false;

        for (int n=1; n<nums.length; n++){
            dp[n] = Math.max(dp[n-1]-1, nums[n]);

            // early exit
            if (dp[n] <= 0 && n != nums.length - 1){
                return false;
            }
        }

        return dp[nums.length -1] >= 0;
    }
}