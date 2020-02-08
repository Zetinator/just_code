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
		Node<T> head;
	public:
		LinkedList();
		LinkedList(int _data);
		LinkedList(std::vector<T> _data);
};

} // namespace Node


