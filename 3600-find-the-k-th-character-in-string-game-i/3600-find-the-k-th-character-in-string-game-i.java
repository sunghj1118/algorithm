class Solution {
    public char kthCharacter(int k) {
        String word = "a";
        String newWord = word;

        while (newWord.length() < k){
            for (char c : word.toCharArray()){
                newWord += (char) (c+1);
            }
            word = newWord;
        }
        return newWord.charAt(k-1);
    }
}