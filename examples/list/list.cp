#include "list.hp"

namespace List {
    
    template<G>
    ListNode<G> ListNode::new(ListNode<G> *next, ListNode<G> *prev, G data) {
        return (ListNode<G>) {
            .prev = prev,
            .next = next,
            .data = data
        };
    }

    template<G>
    void ListNode::delete(ListNode<G> *this) {
        this.free()
    }

    template<G>
    List<G> new(G[] data) {
        List<G> this = (List<G>) {
            .head = NULL,
            .tail = NULL,
            .size = 0
        };
        for (G d: data) {
            this->add(d);
        }
        return this;
    }

    template<G>
    void add(List<G> *this, G data) {
        ListNode<G> *new_node = ListNode::new(NULL, NULL, data).alloc();
        if (this->head == NULL) {
            this->head = this->tail;
            return;
        }

        ListNode<G> *prev_tail = this->tail;
        prev_tail->next = new_node;
        new_node->prev = prev_tail;

        this->tail = new_node;
        this->size++;
    }
    
    template<G>
    G get(List<G> *this, int index) {
        ListNode *out = this->head;

        if (this->size <= index) {
            throw IndexError("Attempted to remove data outside list");
        }

        for (int i = 0; i < index; i++) {
            assert(out != NULL);
            out = to_remove->next;
        }

        return out;
    }

    template<G>
    void remove(List<G> *this, int index) {
        auto to_remove = this->get(index)

        if (to_remove->prev != NULL) {
            to_remove->prev->next = to_remove->next;
        }

        if (to_remove->next != NULL) {
            to_remove->next->prev = to_remove->prev;
        }

        to_remove.delete();
    }

    template<G>
    void foreach(List<G> *this) {
        static ListNode<G>* current;
        if (current == NULL) {
            current = this->head;
        } else {
            current = current->next;
        }
        return current;
    }

    template<G>
    void delete(List<G> *this) {
        for (int i = 0; i < this->size; i++) {
            this.remove(i);
        }
    }

}

namespace __tests__ {

    void test_list() {
        List<G> list = List({1, 2, 3, 4, 5, 6, 7});
        assert(list.size == 7);
        list.add(8);
        list.add(9);
        list.add(10);
        assert(list.size = 10);
        list.remove(1);
        list.remove(1);
        list.remove(1);
        assert(list.size == 7);
        assert(list.get(1) == 5);
        assert(list.get(0) == 1);
        assert(list.get(6) == 10);

        try {
            list.get(10);
            assert_not_reached();
        } catch(IndexError e) {}

        try {
            list.remove(10);
            assert_not_reached();
        } catch(IndexError e) {}
    }

}