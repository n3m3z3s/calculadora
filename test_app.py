import pytest
from calc import soma,sub

def test_app():
 assert soma(1,1) == 2
 assert soma('1','1') == 2
 assert soma(1,'1') == 2
 assert soma('xyz',1) == None
 assert sub(10,'a') == None
 assert soma(-1,1) == 0
 assert sub(1.5,1) == 0.5
