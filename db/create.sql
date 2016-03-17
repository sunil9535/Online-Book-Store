CREATE TABLE Customer (
	Login_id char(20),
	Name VARCHAR(50),
	Password VARCHAR(16),
	Major_credit_card_num text,
	Address VARCHAR(100),
	Phone_num text,
	PRIMARY KEY (Login_id));

CREATE TABLE Books(
	ISBN char(20),
	Title VARCHAR (100),
	Authors VARCHAR (100),
	Publisher VARCHAR (100),
	YOP DATE,
	Category_id varchar(100),
	Available_copies int,
	Price DOUBLE(4,2),
	Format ENUM('Softcover', 'Hardcover'),
	Keywords VARCHAR (100),
	Subject VARCHAR (50),
	PRIMARY KEY (ISBN),
	FOREIGN KEY Category_id REFERENCES Category(cat_id));

CREATE TABLE Orders(
	Order_id int NOT NULL AUTO_INCREMENT,
	timestamp timestamp not null,
	login_id char(20),
	Status ENUM('In transit to Customer', 'Processing Payment','Delivered to Customer','In Warehouse'),
	PRIMARY KEY (Order_id),
	FOREIGN KEY (login_id) REFERENCES Customer(Login_id) ON DELETE CASCADE);

CREATE TABLE Order_book(
	ISBN CHAR(14) ,
	Copies_ordered int,
	Order_id int NOT NULL,
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN) ON DELETE CASCADE,
	FOREIGN KEY (Order_id) REFERENCES Orders(Order_id) ON DELETE CASCADE);

CREATE TABLE Feedback(
	Login_id char(20),
	ISBN CHAR(14),
	Score int CHECK (score <= 10 AND score >= 0),
	Date DATE,
	Short_text VARCHAR(140),
	PRIMARY KEY (Login_id, ISBN),
	FOREIGN KEY (Login_id) REFERENCES Customer(Login_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN));

CREATE TABLE rating( 
	Score int CHECK (Score <= 2 AND Score>=0) ,
	Rater_id CHAR(10),
	Ratee_id CHAR(10),
	ISBN CHAR (14),
	PRIMARY KEY(ISBN, Rater_id, Ratee_id),
	FOREIGN KEY (Rater_id) REFERENCES Customer(Login_id),
	FOREIGN KEY (Ratee_id) REFERENCES Feedback(Login_id));

CREATE TABLE Category(
	cat_id int NOT NULL AUTO_INCREMENT,
	cat_name VARCHAR(100) NOT NULL,
	parent INT,
	PRIMARY KEY (cat_id)
)

CREATE TABLE Sub_Category(
	sub_cat_id int not null AUTO_INCREMENT,
	cat_id int,
	sub_cat_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(sub_cat_id),
	FOREIGN KEY (cat_id) REFERENCES Category(cat_id)
);