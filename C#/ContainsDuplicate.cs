public class Solution {
    public bool ContainsDuplicate(int[] nums)
    {
        HashSet<int> mySet = new();

        foreach (var num in nums)
        {
            if (mySet.Contains(num)) return true;
            mySet.Add(num);
        }
        
        return false;
    }
}