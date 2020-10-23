import java.util.Scanner;
import java.util.*;

class Main {
  private static void solution(int sizeOfMatrix, int[][] matrix) {
    // TODO: 이곳에 코드를 작성하세요.
        boolean [][] visited = new boolean [sizeOfMatrix][sizeOfMatrix];
        int [] dx = {0,1,0,-1};
        int [] dy = {1,0,-1,0};
        ArrayList<Integer> counts = new ArrayList<Integer>();
        for(int x = 0; x < sizeOfMatrix; x++){
            for(int y=0; y < sizeOfMatrix; y++){
                if ((matrix[x][y] == 1) && (!visited[x][y])){
                    // Queue는 인터프리터이기 때문에 직접 쓰지 못하고 뒤에 LinkedList와 같이 파생된 자료형으로 캐스팅해서 사용해야함
                    Queue<int[]> q = new LinkedList<int[]>();
                    q.offer(new int[]{x,y});
                    visited[x][y] = true;
                    int count = 1;
                    while(!q.isEmpty()){
                        int [] temps = q.poll();
                        for (int i = 0; i < 4; i++){
                            int a = temps[0] + dx[i];
                            int b = temps[1] + dy[i];
                            if (a >= 0 && a < sizeOfMatrix && b >= 0 && b < sizeOfMatrix){
                                if(matrix[a][b] == 1 && !visited[a][b]){
                                    count += 1;
                                    visited[a][b] = true;
                                    q.offer(new int[]{a,b});
                                }
                            }
                        }
                    }
                    if(count != 0) {
                        counts.add(count);
                    }
                }
            }
        }
        int n = counts.size();
        if (n == 0){
            System.out.println(0);
        }else{
            System.out.println(n);
            int [] answer = new int[n];
            for(int idx = 0; idx < n; idx++){
                answer[idx] = counts.get(idx);
            }
            Arrays.sort(answer);
            for(int item : answer){
                System.out.print(item + " ");
            }
            System.out.println("");
        }
    }

	
  
  private static class InputData {
    int sizeOfMatrix;
    int[][] matrix;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      
      
      inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
      for (int i = 0; i < inputData.sizeOfMatrix; i++) {
        String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
        for (int j = 0; j < inputData.sizeOfMatrix; j++) {
          inputData.matrix[i][j] = Integer.parseInt(buf[j]);
        }
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.sizeOfMatrix, inputData.matrix);
  }
}