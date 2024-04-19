class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        HashSet<ArrayList> set = new HashSet<>();
        
        for (int i=0; i<grid.length; i++){
            for (int j=0; j<grid[0].length; j++){
                ArrayList<String> tmp = new ArrayList<>();
                tmp.add(Integer.toString(i));
                tmp.add(Integer.toString(j));
                if (!set.contains(tmp) && grid[i][j] == '1'){
                    count++;
                    dfs(i, j, set, grid);
                }
            }
        }
        return count;
    }
    
    public void dfs(int i, int j, HashSet<ArrayList> set, char[][] grid){
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == '0' || set.contains(new ArrayList<>(List.of(Integer.toString(i), Integer.toString(j))))) return;
        
        ArrayList<String> tmp = new ArrayList<>();
        tmp.add(Integer.toString(i));
        tmp.add(Integer.toString(j));
        set.add(tmp);
        
        dfs(i, j+1, set, grid);
        dfs(i, j-1, set, grid);
        dfs(i+1, j, set, grid);
        dfs(i-1, j, set, grid);
    }
}