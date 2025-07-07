class Solution {
    public int maxEvents(int[][] events) {
        // sort by ending time, then by starting time
        Arrays.sort(events, (a,b) -> {
            if (a[1] != b[1]) {
                return Integer.compare(a[1], b[1]);
            } else {
                return Integer.compare(a[0], b[0]);
            }
        });


        int maxEnd = 0;
        for (int[] event : events) maxEnd = Math.max(maxEnd, event[1]);

        TreeSet<Integer> days = new TreeSet<>();
        for (int d=1; d<=maxEnd; d++) days.add(d);
        
        int count = 0;

        for (int[] event : events){
            Integer day = days.ceiling(event[0]);
            if (day != null && day <= event[1]){
                count++;
                days.remove(day);
            }
        }
        
        return count;
    }
}