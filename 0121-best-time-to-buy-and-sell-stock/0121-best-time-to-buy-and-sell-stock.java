// 이때, 딱 한번만 주식을 사고 팔 수 있으니까, 최대 이익을 확인해야 한다.
// 최댓값과 최솟값을 구해야 한다.
// 이어서, 합산 가격을 다 합하면 된다.

class Solution {
	public int maxProfit(int[] prices) {
		int min = Integer.MAX_VALUE;
        int profit = 0;

		for (int i=0; i<prices.length; i++) {
			if (prices[i] < min) {
				min = prices[i];
			} else if (prices[i] - min > profit) {
                profit = prices[i] - min;
			}
		}
		return profit;
	}
}