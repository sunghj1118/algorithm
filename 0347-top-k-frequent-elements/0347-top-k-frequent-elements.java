class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Counter implementation with maps
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
            map.put(num, map.getOrDefault(num,0) + 1);
        }

        // Sort by Highest using EntrySet, Stream, comparingByValue
        List<Integer> topK = map.entrySet()
            .stream()
            .sorted(Map.Entry.<Integer,Integer>comparingByValue(Comparator.reverseOrder()))
            .limit(k)
            .map(Map.Entry::getKey)
            .toList();

        // Get Top K using Int Array
        int[] result = new int[topK.size()];
        for (int i=0; i<topK.size();i++){
            result[i] = topK.get(i);
        }

        // return result
        return result;
    }
}