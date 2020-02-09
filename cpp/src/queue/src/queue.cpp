#include "queue/queue.h"

namespace queue
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
Queue<T>::Queue() {}

template<typename T>
Queue<T>::Queue(const std::vector<T>& data) {
	for(auto e: data)
		this->enqueue(e);
}

template<typename T>
void Queue<T>::enqueue(const T& key) {
	//special case: empty list
	if(!this->head){
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->tail = this->head;
		return;
	}
	//special case: single item
	if(this->head == this->tail) {
		this->head->next = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->tail = this->head->next;
		return;
	}
	//general case
	this->tail->next = std::shared_ptr<Node<T>>(new Node<T>(key));
	this->tail = this->tail->next;
}

template<typename T>
std::shared_ptr<Node<T>> Queue<T>::dequeue() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	auto tmp = this->head;
	this->head = this->head->next;
	return tmp;
}

template<typename T>
std::shared_ptr<Node<T>> Queue<T>::peek() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	return this->head;
}

} // namespace queue

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8};
	auto linked = queue::Queue<int>(test);
	auto node = linked.dequeue();
	if(node)
		std::cout << "dequeued: " << std::to_string(node->value) << std::endl;
	node = linked.peek();
	if(node)
		std::cout << "peeked: " << std::to_string(node->value) << std::endl;
	return 0;
}
