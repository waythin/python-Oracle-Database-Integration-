SELECT FILLINGID,FILLINGNAME from Filling ORDER BY FILLINGCALORIES;

SELECT store.postcode, manager.firstname || ' ' || manager.lastname FROM Store 
INNER JOIN Manager ON store.mangerid=Manager.mangerid ORDER BY store.postcode;

SELECT ORDERPLACE.ORDERID, BREAD.BREADTYPE FROM ORDERPLACE 
INNER JOIN BREAD ON ORDERPLACE.BREADID=BREAD.BREADID
WHERE completion_mark = 'Y';