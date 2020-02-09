#include <bits/stdc++.h>

namespace queue
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
 * Standard Queue implementation.
 * https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
 *
 * the ADT contains the following methods:
 * - enqueue: push a new element into the queue
 * - dequeue: pop a new element from the queue
 * - peek: quick look into the the next element from the queue
 *
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class Queue {
	private:
		std::shared_ptr<Node<T>> head = nullptr;
		std::shared_ptr<Node<T>> tail = head;
	public:
		Queue();
		Queue(const std::vector<T>& _data);
	public:
		void enqueue(const T& key);
		std::shared_ptr<Node<T>> dequeue();
		std::shared_ptr<Node<T>> peek();
};

} // namespace Node


