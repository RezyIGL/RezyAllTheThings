public class Solution {
    public int FirstUniqChar(string s) {
        Dictionary<char, int> freqs = new();

        foreach (var c in s)
        {
            freqs[c] = freqs.ContainsKey(c) ? freqs[c] + 1 : 1;
        }

        foreach (var k in freqs)
        {
            if (freqs[k.Key] == 1) return s.IndexOf(k.Key);
        }
        
        return -1;
    }
}