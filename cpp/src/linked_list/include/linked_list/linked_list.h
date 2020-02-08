#include <bits/stdc++.h>

namespace linked_list
{

template<typename T>
class LinkedList {
	private:
		struct Node {T value; Node* next;};
		Node head;
	public:
		LinkedList(std::vector<T> data);
		// print operator
		operator std::string();
		Node insert();
		Node search();
		void erase();
};

} // namespace Node


