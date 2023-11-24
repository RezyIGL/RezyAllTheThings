public class Solution {
    public int MaxPower(string s) {
        if (s.Equals(string.Empty)) return 0;
        if (s.Length == 1) return 1;
        
        char currChar = s[0];
        int maxSubstrLen = 0;
        int cnt = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != currChar)
            {
                currChar = s[i];
                maxSubstrLen = Math.Max(maxSubstrLen, cnt);
                cnt = 0;
            }
            cnt++;
        }
        
        maxSubstrLen = Math.Max(maxSubstrLen, cnt);
        
        return maxSubstrLen;
    }
}