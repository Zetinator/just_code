#include <bits/stdc++.h>

namespace queue
{

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


