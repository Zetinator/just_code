#include <bits/stdc++.h>

namespace linked_list
{

template<typename T>
class Node {
  private:
    T value;
    Node next;
  public:
    Node(T value);
    ~Node();
    // print operator
    operator std::string();
};
    
template<typename T>
class LinkedList {
  private:
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


