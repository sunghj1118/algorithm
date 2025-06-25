class Solution {
    public boolean isPalindrome(int x) {
        // negative values are false
        if (x<0) return false;

        int reverse = 0;
        int original = x;

        while(x!=0){
            reverse = reverse*10 + x%10;
            x /= 10;
        }

        return reverse == original;
    }
}