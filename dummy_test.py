import dummy

def test1():
    actualDefinition = dummy.getNum()
    expectedDefinition = 2 
    expectedDefinition2 = 3 
    assert actualDefinition == expectedDefinition or actualDefinition == expectedDefinition2