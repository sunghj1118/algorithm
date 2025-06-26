class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();

        for(int i=0;i<s.length();i++){
            if(!stack.isEmpty()){
                if( (stack.peek().equals("(") && String.valueOf(s.charAt(i)).equals(")"))
                 || (stack.peek().equals("[") && String.valueOf(s.charAt(i)).equals("]"))
                 || (stack.peek().equals("{") && String.valueOf(s.charAt(i)).equals("}"))
                ){
                    stack.pop();
                    continue;
                }
            }
            stack.push(String.valueOf(s.charAt(i)));
        }

        if(stack.isEmpty()){
            return true;
        }
        else{
            return false;
        }
    }
}