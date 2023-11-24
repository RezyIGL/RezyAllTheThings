public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var s = "";

        var i = 0;
        var j = 0;

        while (i < word1.Length && j < word2.Length) {
            s += word1[i].ToString() + word2[j].ToString();
            i++;
            j++;
        }

        while (i < word1.Length) {
            s += word1[i].ToString();
            i++;
        }

        while (j < word2.Length) {
            s += word2[j].ToString();
            j++;
        }

        return s;
    }
}