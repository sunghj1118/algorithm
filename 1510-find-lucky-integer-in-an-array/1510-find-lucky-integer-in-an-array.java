class Solution {
    public class Counter<T> {
        private final Map<T, Integer> counts = new HashMap<>();

        public void add(T t){
            counts.merge(t, 1, Integer::sum);
        }

        public int count(T t){
            return counts.getOrDefault(t,0);
        }

        public Set<T> keySet() {
            return counts.keySet();
        }
    }
    
    public int findLucky(int[] arr) {
        Counter<Integer> counter = new Counter<>();
        for(int a : arr){
            counter.add(a);
        }

        ArrayList<Integer> res = new ArrayList<>();
        for (Integer a : counter.keySet()){
            if (counter.count(a) == a){
                res.add(a);
            }
        }

        if (res.isEmpty()) return -1;
        return Collections.max(res);
    }
}