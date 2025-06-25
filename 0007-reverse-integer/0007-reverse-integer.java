class Solution {
    public int reverse(int x) {
        boolean isNegative = false;
        if(x<0){
            isNegative = true;
        }
        x = Math.abs(x);
        
        // get the reverse
        int reverse = 0;
        while(x!=0){
            int digit = x % 10;
            
            // check if outofbounds
            if (reverse < Integer.MIN_VALUE/10 || reverse > Integer.MAX_VALUE/10){return 0;}

            reverse = reverse*10 + digit;
            x /= 10;
        }
        
        // check if negative
        if(isNegative){
            reverse = reverse * (-1);
        }

        
        return reverse;
    }
}