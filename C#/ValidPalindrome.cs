public class Solution {
    public bool IsPalindrome(string s)
    {

        StringBuilder temp = new();
        for (int it = 0; it < s.Length; it++)
        {
            var c = s[it];
            if (char.IsLetter(c)) temp.Append(c.ToString().ToLower());
            else if (char.IsDigit(c)) temp.Append(c.ToString());
        }

        int i = 0;
        int j = temp.Length - 1;

        while (i < j)
        {
            if (!temp[i].Equals(temp[j])) return false;
            i++;
            j--;
        }

        return true;
    }
}