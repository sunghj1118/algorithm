class Solution {
    public boolean isPalindrome(int x) {
        int reverse = 0;
        int original = x;

        // negative values are false
        if (x<0){
            return false;
        }

        while(x!=0){
            reverse = reverse*10 + x%10;
            x /= 10;
        }

        System.out.println(reverse + " " + original);
        if(reverse == original){
            return true;
        }
        else{
            return false;
        }
    }
}