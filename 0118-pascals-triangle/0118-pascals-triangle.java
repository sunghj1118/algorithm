class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pyramid = new ArrayList<>();

        for (int i=0; i<numRows; i++){
            List<Integer> row = new ArrayList<>();

            row.add(1);
            for (int j=1; j<i; j++){
                int val = pyramid.get(i-1).get(j) + pyramid.get(i-1).get(j-1);
                row.add(val);
            }
            if (i>0) row.add(1);

            pyramid.add(row);
        }

        return pyramid;
    }
}