import pytest
from calc import soma,sub,multi,div
def test_app():
 assert soma(1,1) == 2
 assert soma('1','1') == 2
 assert soma(1,'1') == 2
 assert soma('xyz',1) == None
 assert soma(-1,1) == 0
 assert sub(10,'a') == None
 assert sub(1.5,1) == 0.5
 assert sub(2.5,'1') == 1.5
 assert sub(2.5,'a') == None
 assert multi('a',0) == None
 assert multi(-1,1) == -1
 assert multi(-3,-2) == 6
 assert multi(3e2,2) == 600
 assert multi(2e2,'2') == 400
 assert multi('1e2e2',4) == None
 assert multi('2e2',3) == 600
 assert div(2,0) == None
 assert div('4',0) == None
 assert div('3',1) == 3
 assert div('3','3') == 1
 assert div('abc','bca') == None
 assert div('a',1) == None
 assert div('a','a') == None

