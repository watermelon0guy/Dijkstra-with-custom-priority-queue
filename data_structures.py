import math


# эта функция полный мусор.
def tree_print(tree: list):
    levels = int(math.log(len(tree), 2)) + 1
    pos = 0
    line_margin = 2 ** (levels - 1) * 4 // 2
    print("  ", end="")
    for lvl in range(levels):
        print(line_margin * " ", end="")
        line_margin -= 4 * lvl
        for j in range(2 ** lvl):
            if pos == len(tree):
                break
            margin = " " if (j + 1) % 2 == 0 else " "
            print(("%3d" % tree[pos]) + margin, end="")
            pos += 1
        print()


def pq_push(heap, item):
    heap.append(item)
    float_element(heap, 0, len(heap) - 1)


def pq_pull(heap):
    top = heap.pop()
    if heap:
        return_item = heap[0]
        heap[0] = top
        drown_element(heap, 0)
        return return_item
    return top


def float_element(heap, start_pos, pos):
    new_item = heap[pos]
    while pos > start_pos:
        parent_pos = (pos - 1) >> 1
        parent = heap[parent_pos]
        if new_item < parent:
            heap[pos] = parent
            pos = parent_pos
            continue
        break
    heap[pos] = new_item


def drown_element(heap, pos):
    end_pos = len(heap)
    start_pos = pos
    new_item = heap[pos]
    child_pos = 2 * pos + 1
    while child_pos < end_pos:
        right_pos = child_pos + 1
        if right_pos < end_pos and not heap[child_pos] < heap[right_pos]:
            child_pos = right_pos
        heap[pos] = heap[child_pos]
        pos = child_pos
        child_pos = 2 * pos + 1
    heap[pos] = new_item
    float_element(heap, start_pos, pos)
