class Solution {    
    public int findLucky(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int a : arr){
            freq.put(a, freq.getOrDefault(a,0) + 1);
        }

        int res = -1;

        for (int key : freq.keySet()){
            if (freq.get(key) == key){
                res = Math.max(res, key);
            }
        }

        return res;
    }
}