class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length()-1;

        while (end >= 0 && s.charAt(end) == ' '){
            end--;
        }

        int length = 0;
        while (end >= 0 && s.charAt(end) != ' '){
            length++;
            end--;
        }
        return length;
    }
}