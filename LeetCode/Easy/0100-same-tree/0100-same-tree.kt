/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        // 어떤 탐색이든 진행하여 
        // 탐색 순서가 같고
        // 그 값도 같은지 확인
        return compareRecursive(p, q)
    
    }

    private fun compareRecursive(p: TreeNode?, q: TreeNode?): Boolean {
        if (p === q) return true
        if (p == null || q == null) return false
        if (p.`val` != q.`val`) return false

        return compareRecursive(p.left, q.left) && compareRecursive(p.right, q.right)
    }
}