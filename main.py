# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    if (left + right) in ["()", "[]", "{}"]:
        return 1
    else:
        return 0

def find_mismatch(text):
    mismatch=0
    over=0
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            right=next
            if are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char,right)==0:
                over=i+1
                break
            else:
                opening_brackets_stack.pop()
    if over==0:
        if len(opening_brackets_stack)>0:
            mismatch=opening_brackets_stack[0].position+1
        else:
            mismatch="Success"
        return mismatch
    else:
        return over
    
            # Process closing bracket, write your code here


def main():
    choose=input()
    choose_arr=[]
    for i,next in enumerate(choose):
        choose_arr.append(next)
    if choose_arr[0]=="I":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    elif choose_arr[0]=="F":
        f=open("test.txt","r")
        text=f.read()
        mismatch=find_mismatch(text)
        print(mismatch)
    
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
