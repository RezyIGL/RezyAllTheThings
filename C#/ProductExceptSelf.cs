public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var semiSolution = 1;
        var zeroes = 0;
        foreach (var i in nums) {
            if (i != 0){
                semiSolution *= i;
            } else {
                zeroes++;
            }
        }
        int[] result = new int[nums.Length];
        for (int i = 0; i != nums.Length; ++i) {
            if (zeroes == 1) {
                if (nums[i] == 0) {
                    result[i] = semiSolution;
                } else {
                    result[i] = 0;
                }
            } else if (zeroes > 1) {
                result[i] = 0;
            } else {
                result[i] = semiSolution / nums[i];
            }
        }

        return result;
    }
}