class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        #print("Input: {}".format(self._print(head)))
        # Zero or One entry
        if head is None or head.next is None:
            return head

        before_insert = head
        insert = before_insert.next
        after_insert = insert.next

        while insert:
            before_comp = None
            after_comp = head
            inserted = False

            while before_comp is not insert:
                #print("{} insert:{} after_comp:{}".format(self._print(head), insert.val, after_comp.val))

                if before_comp is None:
                    # we are at head
                    if insert.val <= after_comp.val:
                        # insert to the head

                        # before, after pointers for insert
                        before_insert.next = insert.next
                        insert.next = after_comp

                        # head pointer
                        head = insert
                        #print("Inserted {} at head {}".format(insert.val, self._print(head)))
                        inserted = True
                        break
                else:
                    if insert.val > before_comp.val and insert.val <= after_comp.val and after_comp is not insert:
                        # insert
                        before_insert.next = insert.next

                        # before, after pointers for insert
                        before_comp.next = insert
                        insert.next = after_comp

                        #print("Inserted {} at between {} and {}  {}".format(insert.val, before_comp.val, after_comp.val, self._print(head)))
                        inserted = True
                        break

                before_comp = after_comp
                after_comp = after_comp.next
                #print("before_comp:{} after_comp:{}".format(before_comp.val, after_comp.val))


            if not inserted:
                before_insert = before_insert.next

            insert = after_insert

            if after_insert:
                after_insert = after_insert.next
            #print("{} before_insert:{} insert:{} after_insert:{}".format(self._print(head), before_insert.val, insert.val, after_insert.val))

        #print("Output: {}".format(self._print(head)))
        return head

    def _print(self, head):
        curr = head
        output = "head"
        while curr:
            output += "->" + str(curr.val)
            curr = curr.next

        return output
