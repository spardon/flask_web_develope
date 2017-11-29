#!/usr/bin/env python
# -*- coding:utf-8 -*-

def quick_sort(li):
    """
        快速排序
    """
    if len(li) <= 1:
        return li

    site = li.pop()
    l_li = [o for o in li if o < site]
    r_li = [o for o in li if o >= site]
    
    return quick_sort(l_li) + [site] + quick_sort(r_li)


def main():
    li = [6,1,2,7,9,3,4,5,10,8]

    print quick_sort(li)


if __name__ == '__main__':
    main()
