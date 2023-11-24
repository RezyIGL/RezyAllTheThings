public class Solution {
    public int FindMin(int[] nums) {
        int leftPointer = 0;
        int rightPointer = nums.Length - 1;

        while (leftPointer < rightPointer) {
            int mid = (leftPointer + rightPointer) / 2;
            if (nums[mid] < nums[rightPointer]) {
                rightPointer = mid;
            } else {
                leftPointer = mid + 1;
            }
        }
        
        return nums[leftPointer];
    }
}