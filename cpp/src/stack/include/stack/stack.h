#include <bits/stdc++.h>

namespace stack
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


