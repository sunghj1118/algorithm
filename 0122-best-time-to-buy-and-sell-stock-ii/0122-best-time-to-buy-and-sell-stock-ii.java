class Solution {
    public int maxProfit(int[] prices) {
        // calculate the differences between days
        // 7 -> 1 = -6
        // -6,4,-2,3,-2
        // buy when positive
        int profit = 0;

        for(int i=1;i<prices.length;i++){
            if(prices[i-1] < prices[i]){
                profit += prices[i] - prices[i-1];
            }
        }

        return profit;
    }
}