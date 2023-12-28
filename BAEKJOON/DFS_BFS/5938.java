import java.util.ArrayList;
import java.util.Scanner;

public class MisbehavingCows {
    private static ArrayList<Integer>[] graph;
    private static int[] check;

    public static void dfs(int node) {
        check[node] = 1;
        for (int n : graph[node]) {
            if (check[n] == 0) {
                dfs(n);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        graph = new ArrayList[N + 1];
        check = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        dfs(1);

        boolean misbehavingCowsExist = false;

        for (int i = 1; i <= N; i++) {
            if (check[i] == 0) {
                System.out.println(i);
                misbehavingCowsExist = true;
            }
        }

        if (!misbehavingCowsExist) {
            System.out.println(0);
        }

        sc.close();
    }
}
