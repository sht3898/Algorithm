import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int c=0; c<commands.length; c++){
            ArrayList<Integer> arr = new ArrayList<Integer>();

            for(int idx=commands[c][0]-1; idx<commands[c][1]; idx++){
                arr.add(array[idx]);
            }
            Collections.sort(arr);
            answer[c] = arr.get(commands[c][2]-1);
        }
        return answer;
    }
}
