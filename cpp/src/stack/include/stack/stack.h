#include <bits/stdc++.h>

namespace stack
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
 * Standard Stack implementation.
 * https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
 *
 * the ADT contains the following methods:
 * - push: push a new element into the stack
 * - pop: pop a new element from the stack
 * - peek: quick look into the the next element from the stack
 *
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class Stack {
	private:
		std::shared_ptr<Node<T>> head = nullptr;
	public:
		Stack();
		Stack(const std::vector<T>& _data);
	public:
		void push (const T& key);
		std::shared_ptr<Node<T>> pop();
		std::shared_ptr<Node<T>> peek();
};

} // namespace Node


