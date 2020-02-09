#include <bits/stdc++.h>

namespace double_linked_list
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
		std::shared_ptr<Node<T>> previous = nullptr;
};

template<typename T>
class DoubleLinkedList {
	private:
		std::shared_ptr<Node<T>> head = nullptr;
		std::shared_ptr<Node<T>> tail = head;
	public:
		DoubleLinkedList();
		DoubleLinkedList(const std::vector<T>& _data);
	public:
		void append(const T& key);
		std::shared_ptr<Node<T>> search(const T& key);
		std::shared_ptr<Node<T>> pop_back();
		std::shared_ptr<Node<T>> pop_front();
		void insert (const T& key, int index);
		void erase(const T& key);
		void traverse();
};

} // namespace Node


