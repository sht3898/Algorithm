class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[n];

        for (int i=0; i<n; i++){
            if(visit[i] == false){
                dfs(i, n, computers, visit);
                answer++;
            }


        }
        return answer;
    }
    public void dfs(int x, int n, int[][] computers, boolean[] visit){
        visit[x] = true;
        for(int i=0; i<n; i++){
            if (visit[i] == false && computers[x][i] == 1){
                dfs(i, n, computers, visit);
            }
        }
    }
}