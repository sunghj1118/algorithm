import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {

    private static boolean checkIfConnected(int numberOfSites, int[][] connections) {

        /*
         * Your program should set the following variable to true if the graph formed
         * by the specified onnections is connected, i.e., there is a path from every
         * site to every other site.
         */
        boolean isConnected = false;

        /* ------------------- INSERT CODE HERE --------------------- */
        // Create graph using adjacency list representation
        ArrayList<Integer>[] graph = new ArrayList[numberOfSites];
        for (int i = 0; i < numberOfSites; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int[] connection : connections) {
            int site1 = connection[0];
            int site2 = connection[1];
            graph[site1].add(site2);
            graph[site2].add(site1);
        }

        // DFS
        boolean[] visited = new boolean[numberOfSites];
        dfs(graph, 0, visited);

        for (int i = 0; i < numberOfSites; i++) {
            if (!visited[i]) {
                return false;
            }
        }

        /* -------------------- END OF INSERTION -------------------- */

        return true;
    }

    private static void dfs(ArrayList<Integer>[] graph, int node, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(graph, neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numCases = sc.nextInt();

        for (int i = 0; i < numCases; i++) {
            int numberOfSites = sc.nextInt();
            int numberOfConnections = sc.nextInt();

            int[][] connections = new int[numberOfConnections][2];

            for (int j = 0; j < numberOfConnections; j++) {
                connections[j][0] = sc.nextInt();
                connections[j][1] = sc.nextInt();
                assert (connections[j][0] < numberOfSites);
                assert (connections[j][1] < numberOfSites);
            }

            if (checkIfConnected(numberOfSites, connections)) {
                System.out.println("Connected.");
            } else {
                System.out.println("Not connected.");
            }
        }
    }
}
