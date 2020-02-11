#include <bits/stdc++.h>

namespace min_heap
{

/**
 * Standard MinHeap implementation with log(h) lookup.
 * where: h is the height of the heap
 *
 * The ADT contains the following methods:
 * - push: push a new node into the heap
 * - peek: returns the min_element of the heap
 * - pop: remove the min element from the heap and return it
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class MinHeap {
	private:
		std::vector<T> root;
	public:
		MinHeap();
		MinHeap(const std::vector<T>& _data);
	public:
		void push(const T& key);
		const T& peek();
		const T& pop();
		void traverse();
};

} // namespace Node


