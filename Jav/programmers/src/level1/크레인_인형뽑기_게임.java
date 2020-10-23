package level1;

import java.util.ArrayList;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int N = board.length;
        ArrayList bag = new ArrayList();
        
        for (int move: moves){
            for (int i=0; i<N; i++){
                
                if (board[i][move-1] != 0){
                    bag.add(board[i][move-1]);
                    board[i][move-1] = 0;
                    
                    if (bag.size() >= 2){
                        if (bag.get(bag.size()-1) == bag.get(bag.size()-2)){
                            bag.remove(bag.size()-1);
                            bag.remove(bag.size()-1);
                            answer += 2;
                        }
                    }
                    break;
                }
            }
        }
        
        return answer;
    }
}