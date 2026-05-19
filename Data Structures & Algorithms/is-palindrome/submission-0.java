class Solution {
    public boolean isPalindrome(String s) {
        
        String s1 = s.replaceAll("[^A-za-z0-9]","").toLowerCase();

        StringBuilder str = new StringBuilder(s1);
        
        str.reverse();

        String s2= str.toString();

        if(s1.equals(s2)){
            return true;
        }
        return false;
    }
}
