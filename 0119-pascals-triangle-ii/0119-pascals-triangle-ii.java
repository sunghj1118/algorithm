class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> pyramid = new ArrayList<>();

        for (int i=0; i<rowIndex+1; i++){
            
            List<Integer> row = new ArrayList<>();

            row.add(1);

            for (int j=1; j<i; j++){
                row.add(pyramid.get(i-1).get(j) + pyramid.get(i-1).get(j-1));
            }

            if (i>0){
                row.add(1);   
            }

            pyramid.add(row);
        }

        return pyramid.get(rowIndex);
    }
}