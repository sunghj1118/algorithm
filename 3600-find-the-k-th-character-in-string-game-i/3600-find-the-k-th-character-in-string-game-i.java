class Solution {
    public char kthCharacter(int k) {
        return helper(k);
    }

    private char helper(int k){
        if (k==1) return 'a';
        int len = 1;
        while (len<k) len *= 2;
        if (k<=len/2){
            return helper(k);
        } else {
            char prev = helper(k-len/2);
            return prev == 'z' ? 'a' : (char) (prev+1);
        }
    }
}