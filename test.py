from app import add, subtract

def test_add():
  assert add(3,6) == 9

def test_subtract():
  assert subtract(7,6) == 1

