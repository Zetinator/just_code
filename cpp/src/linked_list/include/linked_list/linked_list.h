#include <bits/stdc++.h>

namespace linked_list
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
		std::shared_ptr<Node<T>> next = nullptr;
};

/**
 * Standard linked list implementation.
 *
 * the ADT contains the following methods:
 * - append: push a new element into the back of the list
 * - insert: pushes a new element into the given position
 * - search: looks for the element and returns the node if found in O(n)
 * - erase: deletes the node containing the given value from the list
 * - traverse: prints a visual representation of the current list
 *
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class LinkedList {
	private:
		std::shared_ptr<Node<T>> head = nullptr;
	public:
		LinkedList();
		LinkedList(const std::vector<T>& _data);
	public:
		void append(const T& key);
		std::shared_ptr<Node<T>> search(const T& key);
		void insert (const T& key, int index);
		void erase(const T& key);
		void traverse();
};

} // namespace Node


