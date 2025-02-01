from hexlet_pytest.example import reverse
import pytest


def test_stack():
    stack = []

    stack.append("one")
    stack.append("two")

    assert stack.pop() == 'two'

def test_stack2():
    stack = []

    stack.append("one")
    stack.append("two")

    stack.pop()
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert (stack)

    stack.pop()
    assert not stack

def test_popisempty():
    stack = []

    with pytest.raises(IndexError):
        stack.pop()