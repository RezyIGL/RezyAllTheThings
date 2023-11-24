public class Solution {
    public int StrStr(string haystack, string needle) {
        var n = haystack.Length;
        var m = needle.Length;

        if (n == m) if (haystack == needle) return 0;

        for (int i = 0; i <= n - m; ++i)
        {
            if (haystack[i..(i + m)] == needle)
            {
                return i;
            }
        }
        
        return -1;
    }
}