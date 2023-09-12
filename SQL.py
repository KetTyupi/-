SELECT co.login,
       COUNT(ord.track),
FROM "Couriers" AS co
LEFT OUTER JOIN Orders AS ord ON co.id=ord."courierId"
WHERE "inDelivery" = true
GROUP BY co.login;

SELECT track,
CASE 
    WHEN finished == true THEN 2
    WHEN cancelled == true THEN -1
    WHEN "inDelivery" == true THEN 1
    ELSE 0
END
FROM "Orders";


