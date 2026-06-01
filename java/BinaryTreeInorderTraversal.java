class Node {
    int key;
    Node left, right;
    public Node(int item) {
        key = item;
        left = right = null;
    }
}

public class BinaryTreeInorderTraversal {
    Node root;
    BinaryTreeInorderTraversal() { root = null; }

    void printInorder(Node node) {
        if (node == null) return;
        printInorder(node.left);
        System.out.print(node.key + " ");
        printInorder(node.right);
    }

    public static void main(String[] args) {
        BinaryTreeInorderTraversal tree = new BinaryTreeInorderTraversal();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        System.out.println("Inorder traversal of binary tree is: ");
        tree.printInorder(tree.root);
    }
}
