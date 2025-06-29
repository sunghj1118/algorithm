class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str : strs){
            // sort str after making it into char array
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            // if char array exists, add the str to it's respective group
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
