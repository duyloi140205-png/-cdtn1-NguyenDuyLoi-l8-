USE csat_nps;
INSERT INTO Customer(CustomerID,FullName,Phone,Email) VALUES (1,'Khách hàng mẫu','0900000000','sample@example.com') ON DUPLICATE KEY UPDATE FullName=VALUES(FullName);
INSERT INTO Store(StoreID,StoreName,Address) VALUES (1,'Cửa hàng mẫu','TP.HCM') ON DUPLICATE KEY UPDATE StoreName=VALUES(StoreName);
INSERT INTO WarrantyTicket(TicketID,CustomerID,StoreID,CompletedDate,Status) VALUES (1,1,1,CURDATE(),'Completed') ON DUPLICATE KEY UPDATE Status=VALUES(Status);
INSERT INTO Survey(SurveyID,TicketID,SentDate,ExpireDate) VALUES (1,1,CURDATE(),DATE_ADD(CURDATE(),INTERVAL 30 DAY)) ON DUPLICATE KEY UPDATE ExpireDate=VALUES(ExpireDate);
