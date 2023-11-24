public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxEnding = nums[0];
        int max = nums[0];
        for (int i = 1; nums.Length > i; i++)
        {
            maxEnding = Math.Max(nums[i], maxEnding + nums[i]);
            max = Math.Max(max, maxEnding);
        }
        return max;
    }
}