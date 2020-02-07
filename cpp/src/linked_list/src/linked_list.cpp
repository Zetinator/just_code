#include "linked_list/linked_list.h"

namespace linked_list
{
template<typename T>
Node<T>::Node(T v) {
    T value(v);
    Node<T>* next(nullptr_t);
}

template<typename T>
LinkedList<T>::LinkedList(std::vector<T> data) {
    Node<T>* head(nullptr_t);
}

} // namespace Node

// only here for testing
int main(int argc, char const *argv[])
{
    if (argc < 2) {
    // report version
    std::cout << argv[0] << " Version " << "1.0.0" << ".\n";
    std::cout << "Usage: " << argv[0] << " <your name>" << std::endl;
    return 1;
  }
    std::cout << argv[1] << " quiere mucho a su marion :(" << std::endl;
    return 0;
}
