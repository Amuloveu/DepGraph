import pytest
from deepgraph import graph
# 1. No cycle
NO_CYCLE = {
    "main": ["users"],
    "users": ["database"],
    "database": []
}
# Expected: False


# 2. Simple cycle
SIMPLE_CYCLE = {
    "main": ["users"],
    "users": ["main"]
}
# Expected: True


# 3. Disconnected cycle
DISCONNECTED_CYCLE = {
    "main": ["users"],
    "users": [],
    "alpha": ["beta"],
    "beta": ["alpha"]
}
# Expected: True


# 4. Shared dependency (not a cycle)
SHARED_DEPENDENCY = {
    "main": ["users", "payments"],
    "users": ["database"],
    "payments": ["database"],
    "database": []
}
# Expected: False
MISSING_DEPENDENCY = {
    "main": ["users"],
    "users": ["database"]
}
def test_no_cycle():
    assert graph.has_cycle(NO_CYCLE) == False

def test_simple_cycle():
    assert graph.has_cycle(SIMPLE_CYCLE)

def test_disconnected_cycle():
    assert graph.has_cycle(DISCONNECTED_CYCLE)

def test_shared_dependency():
    assert graph.has_cycle(SHARED_DEPENDENCY) == False

def test_missing_dependency():
    assert not graph.has_cycle(MISSING_DEPENDENCY) 
