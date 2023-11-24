public class Solution {
    public int WaysToMakeFair(int[] nums) {
        int answer = 0;
        int oddSumm = 0;
        int evenSumm = 0;
        
        for (int i = 0; i < nums.Length; i++)
        {
            if (i % 2 == 0) evenSumm += nums[i];
            else oddSumm += nums[i];
        }
        
        int prev = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (i % 2 == 0) evenSumm = evenSumm - nums[i] + prev;
            else oddSumm = oddSumm - nums[i] + prev;
            if (evenSumm == oddSumm) answer++;
            prev = nums[i];
        }
        
        return answer;
    }
}