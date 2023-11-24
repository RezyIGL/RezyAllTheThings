class Solution {
    public int maxPower(String s) {
        if (s.length() < 2) return s.length();
        int result = 1;
        int temp = 1;
        for(int i = 0;i<s.length()-1;i++){
            if(s.charAt(i)==s.charAt(i+1)){
                temp++;
            }else{
                result = Math.max(result,temp);
                temp = 1;
            }
        }
        return Math.max(result,temp);
    }
}