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

//template<typename T>
//class LinkedList {
	//private:
		//Node head;
	//public:
		//LinkedList(std::vector<T> data);
		//operator std::string();
		//Node insert();
		//Node search();
		//void erase();
//};

} // namespace Node


