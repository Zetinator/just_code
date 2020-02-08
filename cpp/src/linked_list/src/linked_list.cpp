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
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		return;
	}
	auto node = this->head;
	while(node->next)
		node = node->next;
	node->next = std::shared_ptr<Node<T>>(new Node<T>(key));
}

template<typename T>
std::shared_ptr<Node<T>> LinkedList<T>::search(const T& key) {
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
void LinkedList<T>::insert(const T& key, int index) {
	//special case: empty list
	if(!this->head){
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		return;
	}
	//special case: insert as head
	if(index == 0){
		auto tmp = this->head;
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->head->next = tmp;
		return;
	}
	//general case:
	auto node = this->head;
	while(node->next && (index-1) > 0){
		node = node->next;
		index -= 1;
	}
	auto tmp = node->next;
	node->next = std::shared_ptr<Node<T>>(new Node<T>(key));
	node->next->next = tmp;
}

template<typename T>
void LinkedList<T>::erase(const T& key) {
	//special case: empty list
	if(!this->head)
		return;
	//special case: is head
	if(this->head->value == key){
		this->head = head->next;
		return;
	}
	//general case:
	auto node = this->head;
	auto parent = node;
	while(node) {
		if(node->value == key) {
			parent->next = node->next;
			return;
		}
		parent = node;
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

// only here for testing while we implement hte gtest module
int main(int argc, char const *argv[])
{
	std::vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8};
	auto linked = linked_list::LinkedList<int>(test);
	auto node = linked.search(4);
	int key = 69, index = 3;
	linked.insert(key, index);
	linked.erase(key);
	linked.traverse();
	return 0;
}
