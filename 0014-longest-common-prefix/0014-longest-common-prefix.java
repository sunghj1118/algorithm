class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs==null) return "";
        if (strs.length==1) return strs[0];
        
        String longest = "";
        Arrays.sort(strs, (s1,s2) -> s1.length() - s2.length());
        
        char curr = 'a';
        
        for (int i=0; i<strs[0].length(); i++){
            curr = strs[0].charAt(i);
            for (int j=1; j<strs.length; j++){
                if (strs[j].charAt(i) != curr){
                    return longest;
                }
            }
            longest += curr;
        }

        return longest;
    }
}