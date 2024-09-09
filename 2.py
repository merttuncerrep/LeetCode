'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

def main(l1, l2):

    if len(l1) < 0:
        print(l2)
    if len(l2) < 0:
        print(l1)

    ctr = 0
    isBorrowed = False
    response  = []

    while l1 and l2:


        l1Value = 0 if len(l1) < ctr else l1[ctr]
        l2Value =  0 if len(l1) < ctr else l2[ctr]

        print(str(l1Value) + " " + str(l2Value) + " " + str(response))

        total = l1Value + l2Value + (1 if isBorrowed else 0)
        if (total >= 10):
            isBorrowed = True
            response.append(total - 10)
        else:
            isBorrowed = False
            response.append(total)

        if len(l1) <= ctr + 1 and len(l2) <= ctr + 1:
            if isBorrowed:
                response.append(1)
            break
        ctr = ctr + 1

    print (response)

if __name__ == "__main__":
    main([9,9,9,9,9,9,9], [9,9,9,9])

