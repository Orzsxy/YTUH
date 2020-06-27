/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *pre,*last;
        ListNode *L1 = l1;
        ListNode *L2 = l2;
        int base =0,tmp;
        while(L1&&L2){
            tmp = L1->val+L2->val+base;
            L1 ->val = (tmp)%10;
            base =(tmp)/10;
            pre = L1;
            last =L1;
            L1=L1->next;
            L2=L2->next;
        }
        while(L1){
            tmp =L1->val+base;
            L1 ->val = (tmp)%10;
            base = (tmp)/10;
            last =L1;
            L1= L1->next;
            if(base==0) break;
        }
        if(L2) pre->next = L2;
        while(L2){
            tmp = L2->val+base;
            L2 ->val = (tmp)%10;
            base=(tmp)/ 10;
            last = L2;
            L2= L2->next;
            if(base==0)break;
        }        
        if(base){
            l2->val = base;
            l2->next = NULL;
            last ->next = l2;
        }
        return l1;
    }
};
/*
一个空间都不能申请
爆ll
*/