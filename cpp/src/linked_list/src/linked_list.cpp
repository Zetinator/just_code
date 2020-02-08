#include "linked_list/linked_list.h"

namespace linked_list
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
LinkedList<T>::LinkedList() {}

template<typename T>
LinkedList<T>::LinkedList(const std::vector<T>& data) {
	for(auto e: data)
		this->append(e);
}


template<typename T>
void LinkedList<T>::append(const T& key) {
	if(!this->head){
		this->head = new Node<T>(key);
		return;
	}
	auto node = this->head;
	while(node->next)
		node = node->next;
	node->next = new Node<T>(key);
}

template<typename T>
Node<T>* LinkedList<T>::search(const T& key) {
	if(!this->head)
		return nullptr;
	auto node = this->head;
	while(node){
		if(node->value == key)
			return node;
		node = node->next;
	}
	return nullptr;
}

template<typename T>
void LinkedList<T>::insert(const T& key) {
	if(!this->head)
		return;
	auto node = this->head;
	while(node){
		if(node->value == key)
			return;
		node = node->next;
	}
	return;
}

template<typename T>
void LinkedList<T>::traverse() {
	if(!this->head)
		return;
	auto node = this->head;
	while(node){
		std::cout << "->(" + std::to_string(node->value) << ")";
		node = node->next;
	}
	std::cout << std::endl;
}

} // namespace linked_list

// only here for testing
int main(int argc, char const *argv[])
{
	if (argc < 2) {
		// report version
		std::cout << argv[0] << " Version " << "1.0.0" << ".\n";
		std::cout << "Usage: " << argv[0] << " <your name>" << std::endl;
		return 1;
	}

	//testing...
	std::vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8};
	auto linked = linked_list::LinkedList<int>(test);
	//print list
	linked.traverse();
	auto node = linked.search(4);
	if(node)
		std::cout << "found: " << std::to_string(node->value) << std::endl;
	return 0;
}
