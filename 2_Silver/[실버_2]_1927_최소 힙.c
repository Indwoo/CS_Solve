#include <stdio.h>

int min_heap[10001] = {0,};
int idx = 1;

void insert_heap(int val)
{
    int temp;
    int temp_idx = idx;
    min_heap[idx++] = val;
    while (temp_idx > 1)
    {
        if (min_heap[temp_idx / 2] > min_heap[temp_idx])
        {
            temp = min_heap[temp_idx / 2];
            min_heap[temp_idx / 2] = min_heap[temp_idx];
            min_heap[temp_idx] = temp;
            temp_idx /= 2;
        }
        else
        {
            break;
        }
    }
}

void heapify(int i)
{
    int parent = i;
    int left = i * 2;
    int right = i * 2 + 1;
    int temp;

    if (left < idx && min_heap[left] < min_heap[right])
    {
        parent = left;
    }
    if (right < idx && min_heap[right] < min_heap[left])
    {
        parent = right;
    }
    if (parent != i)
    {
        temp = min_heap[i];
        min_heap[i] = min_heap[parent];
        min_heap[parent] = temp;
        heapify(parent);
    }
}

void main()
{
    int N;
    int temp;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        if (temp == 0)
        {
            if (idx == 1)
            {
                printf("0\n");
            }
            else
            {
                printf("%d\n", min_heap[i]);
                min_heap[1] = min_heap[idx - 1];
                heapify(1);
                idx -= 1;
            }
        }
        else
        {
            insert_heap(temp);
        }
    }
}