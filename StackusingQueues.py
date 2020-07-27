
import atexit
import sys
import io


def push(x):
    global queue_1
    global queue_2
    queue_1.append(x)


def pop():
    global queue_1
    global queue_2
    if len(queue_1) > 0:
        x = queue_1[-1]
        queue_1 = queue_1[:-1]
        return x
    else:
        return -1


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


queue_1 = []  # first queue
queue_2 = []  # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push(a[i+1])
                i += 1
            else:
                print(pop(), end=" ")
            i += 1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
