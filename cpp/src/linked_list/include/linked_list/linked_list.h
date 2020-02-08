#include <bits/stdc++.h>

namespace linked_list
{

template <typename T>
class Node {
	public:
		//constructor
		Node();
		Node(T _value);
		//member variables
		T value;
		Node<T>* next;
};

template<typename T>
class LinkedList {
	private:
		Node<T>* head = nullptr;
	public:
		LinkedList();
		LinkedList(const std::vector<T>& _data);
	public:
		void append(const T& key);
		Node<T>* search(const T& key);
		void insert (const T& key, int index);
		void erase(const T& key);
		void traverse();
};

} // namespace Node


