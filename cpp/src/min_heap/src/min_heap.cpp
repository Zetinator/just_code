#include "min_heap/min_heap.h"

namespace min_heap
{

template<typename T>
MinHeap<T>::MinHeap() {}

template<typename T>
MinHeap<T>::MinHeap(const std::vector<T>& data) {
	for(T e: data)
		this->push(e);
}

template<typename T>
void MinHeap<T>::push(const T& key) {
	//special case: empty heap
	if(this->root.empty()) {
		this->root.push_back(key);
		return;
	}
	//general case:
	auto parent = [&] (int i)->int {
		return ((i-1)/2 > 0)?(i-1)/2:0;
	};
	int i = this->root.size();
	this->root.push_back(key);
	while(this->root[parent(i)] > this->root[i]) {
		std::swap(this->root[parent(i)], this->root[i]);
		i = parent(i);
	}
}

template<typename T>
void MinHeap<T>::traverse() {
	//special case: empty heap
	if(this->root.empty())
		return;
	//general case:
	std::copy(this->root.begin(), this->root.end(),
          std::ostream_iterator<T>(std::cout, " "));
	std::cout << std::endl;
}

template<typename T>
const T& MinHeap<T>::peek() {
	if(this->root.empty())
		throw std::out_of_range("the heap is empty");
	return this->root[0];
}

template<typename T>
const T& MinHeap<T>::pop() {
	//special case: empty heap
	if(this->root.empty())
		throw std::out_of_range("the heap is empty");
	//general case:
	std::swap(this->root[0], this->root[this->root.size()-1]);
	const T& tmp = this->root[this->root.size()-1];
	this->root.pop_back();
	int i = 0;
	auto left = [&] (int i)->int {
		return ((i*2)+1 < static_cast<int>(this->root.size()))?(i*2)+1:this->root.size();
	};
	auto right = [&] (int i)->int {
		return ((i*2)+2 < static_cast<int>(this->root.size()))?(i*2)+2:this->root.size();
	};
	auto test = [&] (int i)-> bool {
		return (i == static_cast<int>(this->root.size())) ? false:true;
	};
	while((test(left(i)) && this->root[left(i)] < this->root[i]) ||
		  (test(right(i)) && this->root[right(i)] < this->root[i])) {
		auto child = left(i);
		//get min of the 2 children
		if(test(left(i)) && test(right(i)) && this->root[left(i)] > this->root[right(i)])
			child = right(i);
		std::swap(this->root[child], this->root[i]);
		i = child;
	}
	return tmp;
}

} // namespace min_heap

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {5,7,0,9,3,2,8};
	auto heap = min_heap::MinHeap<int>(test);
	heap.traverse();
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	std::cout << "pop min: " << std::to_string(heap.pop()) << std::endl;
	heap.traverse();
}
