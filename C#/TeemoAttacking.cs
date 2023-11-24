public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration)
    {
        int seconds = 0;

        for (int i = 0; i < timeSeries.Length; i++)
        {
            if (i == timeSeries.Length - 1)
            {
                seconds += duration;
                break;
            }

            int abiba = timeSeries[i + 1] - timeSeries[i];
            if (abiba >= duration)
            {
                seconds += duration;
            }
            else
            {
                seconds += abiba % duration;
            }
        }
        
        return seconds;
    }
}