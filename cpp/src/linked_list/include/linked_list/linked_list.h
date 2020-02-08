#include <bits/stdc++.h>

namespace linked_list
{

template<typename T>
class LinkedList {
	private:
		class Node;
		Node<T> head;
	public:
		LinkedList(std::vector<T> data);
		~LinkedList();
		// print operator
		operator std::string();
		Node<T> insert();
		Node<T> search();
		void erase();
};

} // namespace Node


