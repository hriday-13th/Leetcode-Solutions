/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }
    public int dfs(TreeNode node, boolean bool){
        if (node == null) return 0;
        if (node.left == null && node.right == null){
            return bool ? node.val : 0;
        }
        
        int left = dfs(node.left, true);
        int right = dfs(node.right, false);
        return left+right;
    }
}