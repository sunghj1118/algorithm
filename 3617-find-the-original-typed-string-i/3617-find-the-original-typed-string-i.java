class Solution {
    public int possibleStringCount(String word) {
        ArrayList<Character> letters = new ArrayList<>();

        for (char w : word.toCharArray()){
            letters.add(w);
        }

        int counter = 1;
        for (int i=1; i<word.length(); i++){
            if (letters.get(i).equals(letters.get(i-1))){
                counter += 1;
            }
        }
        return counter;
    }
}