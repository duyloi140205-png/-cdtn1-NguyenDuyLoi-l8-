CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FullName VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE Store (
    StoreID INT PRIMARY KEY,
    StoreName VARCHAR(100),
    Address VARCHAR(255)
);

CREATE TABLE WarrantyTicket (
    TicketID INT PRIMARY KEY,
    CustomerID INT,
    StoreID INT,
    CompletedDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID)
);

CREATE TABLE Survey (
    SurveyID INT PRIMARY KEY,
    TicketID INT,
    SentDate DATE,
    ExpireDate DATE,
    FOREIGN KEY (TicketID) REFERENCES WarrantyTicket(TicketID)
);

CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY,
    SurveyID INT,
    CSATScore INT,
    NPSScore INT,
    Comment TEXT,
    SubmittedDate DATE,
    FOREIGN KEY (SurveyID) REFERENCES Survey(SurveyID)
);