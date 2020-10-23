import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        // equals는 내용 비교, ==는 주소값 비교
        for (int i=0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])){
            // if (participant[i] != completion[i]){
                return participant[i];
            }
        }
        return participant[participant.length-1];
    }
}