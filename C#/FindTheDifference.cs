public class Solution {
    public char FindTheDifference(string s, string t)
    {
        Dictionary<char, int> dict = new Dictionary<char, int>();

        foreach (var let in t)
        {
            if (dict.ContainsKey(let)) dict[let]++;
            else dict[let] = 1;
        }

        foreach (var let in s)
        {
            dict[let]--;
            if (dict[let] == 0)
            {
                dict.Remove(let);
            }
        }

        char result = default;
        foreach (var key in dict)
        {
            result = key.Key;
        }
        
        return result;
    }
}