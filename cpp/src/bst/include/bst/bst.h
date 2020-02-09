#include <bits/stdc++.h>

namespace bst
{

/**
 * basic chinable storage unit.
 *
 *
 * @tparam T the type of data stored in the bst
 */
template <typename T>
class Node {
	public:
		//constructor
		Node();
		Node(T _value);
		//member variables
		T value;
		std::shared_ptr<Node<T>> left = nullptr;
		std::shared_ptr<Node<T>> right = nullptr;
};

/**
 * Standard BST implementation with log(h) lookup.
 * where: h is the height of the tree
 *
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class BST {
	private:
		std::shared_ptr<Node<T>> root = nullptr;
	public:
		BST();
		BST(const std::vector<T>& _data);
	public:
		void insert(const T& key);
		void insert(const T& key, std::shared_ptr<Node<T>> node);
		std::shared_ptr<Node<T>> search(const T& key);
		std::shared_ptr<Node<T>> search(const T& key, std::shared_ptr<Node<T>> node);
		std::shared_ptr<Node<T>> min();
		std::shared_ptr<Node<T>> max();
		void rotate_left(std::shared_ptr<Node<T>> node);
		void rotate_right(std::shared_ptr<Node<T>> node);
		void erase(const T& key);
		void erase(const T& key,
				std::shared_ptr<Node<T>> node,
				std::shared_ptr<Node<T>> father = nullptr);
		void traverse();
		void traverse(std::shared_ptr<Node<T>> node, int level = 0);
};

} // namespace Node


