class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {return false;}

        char[] s_letters = s.toCharArray();
        char[] t_letters = t.toCharArray();

        Arrays.sort(s_letters);
        Arrays.sort(t_letters);

        return Arrays.equals(s_letters,t_letters);
    }
}
