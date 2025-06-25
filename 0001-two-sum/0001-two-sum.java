class Solution {
    public int[] twoSum(int[] nums, int target) {
        // insert into hash table
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length;i++){
            map.put(nums[i], i);
        }

        // check if complement exists in table
        for (int i=0;i<nums.length;i++){
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement) };
            }
        }


        return new int[]{};
    }
}