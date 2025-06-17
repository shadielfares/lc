class Solution {
    public int search(int[] nums, int target) {
        int lowestPossibleLoc = 0;
        int highestPossibleLoc = nums.length -1;
        while (highestPossibleLoc >= lowestPossibleLoc){
            int middle = (highestPossibleLoc + lowestPossibleLoc) /2;
            if (nums[middle] == target){
                return middle;
            } else if (nums[middle] > target){
                highestPossibleLoc = middle - 1;
            } else{
                lowestPossibleLoc = middle + 1;
            }
        }
        return -1;
    }
}