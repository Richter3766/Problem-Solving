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
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) return true
        return same(root.left, root.right)
    }

    private fun same(left: TreeNode?, right: TreeNode?): Boolean {
        if (left === right) return true
        if (left == null || right == null) return false
        if (left.`val` != right.`val`) return false

        return same(left.left, right.right) && same(left.right, right.left)
    }
}