public class Solution {
    public static int solution(int start, int length) {
        // 0 XOR any number is the number itself so we start at 0 to prevent the first start XOR start
        int res = 0;
        int count = start;
        for (int i = 0; i < length; i++)
        {
            // -i is to skip bunnies to reduce time complexity for i >= length/2
            for (int j = 0; j < length-i; j++)
            {
                res ^= count + j;
            }
            // increment each time to start at a different row
            count += length;
        }
        return res;
    }
}