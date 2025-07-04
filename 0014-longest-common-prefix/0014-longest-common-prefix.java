class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs==null) return "";
        if (strs.length==1) return strs[0];
        
        int minLen = Integer.MAX_VALUE;
        for (String s : strs){
            if (s.length() < minLen){
                minLen = s.length();
            }
        }
        
        StringBuilder prefix = new StringBuilder();
        
        for (int i=0; i<minLen; i++){
            char curr = strs[0].charAt(i);

            for (int j=1; j<strs.length; j++){
                if (strs[j].charAt(i) != curr){
                    return prefix.toString();
                }
            }
            prefix.append(curr);
        }

        return prefix.toString();
    }
}