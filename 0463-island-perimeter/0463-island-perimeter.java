class Solution {
    HashSet<String> seen = new HashSet<>();
    public int islandPerimeter(int[][] grid) {
        for (int i=0; i < grid.length; i++){
            for (int j=0; j < grid[0].length; j++){
                if (grid[i][j] == 1) return dfs(i, j, grid);
            }
        }
        return 0;
    }
    
    public int dfs(int i, int j, int[][] grid){
        if (i<0 || j<0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0) return 1;
        String temp = i + "," + j;
        
        if (seen.contains(temp)) return 0;
        else seen.add(temp);
        
        int ans = 0;
        
        ans += dfs(i+1, j, grid);
        ans += dfs(i-1, j, grid);
        ans += dfs(i, j+1, grid);
        ans += dfs(i, j-1, grid);
        
        return ans;
    }
}