package tree;

public class ArrBinaryTreeDemo {
	public static void main(String[] args) {
		int[] array = {1,2,3,4,5,6,7};
		// 创建一个ArrayBinaryTree
		ArrBinaryTree arrBinaryTree = new ArrBinaryTree(array);
		arrBinaryTree.preOrder(); // 1,2,4,5,3,6,7
	}
}

// 编写一个ArrayBinaryTree，实现顺序存储二叉树遍历
class ArrBinaryTree{
	private int [] array; //存储数据结点的数组
	public ArrBinaryTree(int[] array) {
		this.array = array;
	}
	// 重载preOrder
	public void preOrder() {
		this.preOrder(0);
	}
	
	// 编写一个方法，完成顺序存储二叉树的前序遍历
	// index = 数组下标
	public void preOrder(int index) {
		// 如果数组为空，或者array.length = 0
		if(array.length == 0 || array == null) {
			System.out.println("数组为空，不能按照二叉树的前序遍历");
		}
		// 输出当前这个元素
		System.out.println(array[index]);
		// 向左递归遍历
		// 防止越界
		if((index*2+1)<array.length) {
			preOrder((index*2+1));
		}
		// 向右递归遍历
		// 防止越界
		if((index*2+2)<array.length) {
			preOrder((index*2+2));
		}
	}
}