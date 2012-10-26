# coding=utf-8

"""
.. module:: sort
.. moduleauthor:: zwm <zhaoweiming@hotmail.com>

:platform: Unix, Windows
:synopsis: 排序算法
"""

import random
from copy import copy

def directInsertSort(seq):
    """直接插入排序

    Args:
        seq (list): 要进行排序的列表

    Returns:
        list. 返回的代码 ::

            0 -- 成功！
            1 -- 一般！

    Raises:
        AttributeError, KeyError

    使用方法 ::

        >>> asdfjsaldfjasfdj
        0
        >>> juestisdfjasd
        1
    """
    size = len(seq)
    for i in range(1,size):
        tmp, j = seq[i], i
        while j > 0 and tmp < seq[j-1]:
            seq[j], j = seq[j-1], j-1
        seq[j] = tmp
    return seq

def directSelectSort(seq):
    """ 直接选择排序 """
    size = len(seq)
    for i in range(0,size - 1):
        k = i;j = i+1
        while j < size:
            if seq[j] < seq[k]:
                k = j
            j += 1
        seq[i],seq[k] = seq[k],seq[i]
    return seq

def bubbleSort(seq):
    """冒泡排序"""
    size = len(seq)
    for i in range(1,size):
        for j in range(0,size-i):
            if seq[j+1] < seq[j]:
                seq[j+1],seq[j] = seq[j],seq[j+1]
    return seq

def _divide(seq, low, high):
    """快速排序划分函数"""
    tmp = seq[low]
    while low != high:
        while low < high and seq[high] >= tmp: high -= 1
        if low < high:
            seq[low] = seq[high]
            low += 1
        while low < high and seq[low] <= tmp: low += 1
        if low < high:
            seq[high] = seq[low]
            high -= 1
    seq[low] = tmp
    return low

def _quickSort(seq, low, high):
    """快速排序辅助函数"""
    if low >= high: return
    mid = _divide(seq, low, high)
    _quickSort(seq, low, mid - 1)
    _quickSort(seq, mid + 1, high)

def quickSort(seq):
    """快速排序包裹函数"""
    size = len(seq)
    _quickSort(seq, 0, size - 1)
    return seq

def merge(seq, left, mid, right):
    tmp = []
    i, j = left, mid
    while i < mid and j <= right:
        if seq[i] < seq[j]:
            tmp.append(seq[i])
            i += 1
        else:
            tmp.append(seq[j])
            j += 1
    if i < mid: tmp.extend(seq[i:])
    if j <= right: tmp.extend(seq[j:])

    seq[left:right+1] = tmp[0:right-left+1]

def _mergeSort(seq, left, right):
    if left == right:
        return
    else:
        mid = (left + right) / 2
        _mergeSort(seq, left, mid)
        _mergeSort(seq, mid + 1, right)
        merge(seq, left, mid+1, right)

#二路并归排序
def mergeSort(seq):
    size = len(seq)
    _mergeSort(seq, 0, size - 1)
    return seq

if __name__ == '__main__':
    s = [random.randint(0,100) for i in range(0,20)]
    print s
    print "\n"
    print directSelectSort(copy(s))
    print directInsertSort(copy(s))
    print bubbleSort(copy(s))
    print quickSort(copy(s))
    print mergeSort(copy(s))