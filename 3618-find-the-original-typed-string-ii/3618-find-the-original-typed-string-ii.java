class Solution {
    static final int MOD = 1_000_000_007;
    public int possibleStringCount(String word, int k) {
        int n = word.length();

        if (word == null || word.isEmpty()) return 0;

        // 1. get block lengths
        ArrayList<Integer> lengths = new ArrayList<>();
        int count = 1;
        for (int i=1; i<n; i++){
            if (word.charAt(i) == word.charAt(i-1)){
                count++;
            } else{
                lengths.add(count);
                count = 1;
            }
        }
        lengths.add(count);

        // 2. create dp array
        long totalWays = 1;
        for (int len : lengths){
            totalWays = (totalWays * len) % MOD;
        }

        // if num blocks is already >= k, return totalWays right away
        if (lengths.size() >= k){
            return (int) totalWays;
        }

        // 3. DP arrays for counting number of strings with length < k
        int[] dp = new int[k];
        dp[0] = 1;
    
        for (int len : lengths){
            int[] newDp = new int[k];
            int[] prevPrefix = new int[k];
            prevPrefix[0] = dp[0];
            for (int j=1; j<k; j++){
                prevPrefix[j] = (prevPrefix[j-1] + dp[j]) % MOD;
            }

            for (int j=1; j<k; j++){
                int left = j-len-1;
                int val = prevPrefix[j-1];
                if (left >= 0) {
                    val = (val - prevPrefix[left] + MOD) % MOD;
                }
                newDp[j] = val;
            }

            dp = newDp;
        }


        // 4. Result = totalWays - number of strings with length < k
        int[] finalPrefix = new int[k];
        finalPrefix[0] = dp[0];
        for (int j=1; j<k; j++){
            finalPrefix[j] = (finalPrefix[j-1] + dp[j]) % MOD;
        }

        int result = (int) ((totalWays - finalPrefix[k-1] + MOD) % MOD);
        return result;
    }
}
