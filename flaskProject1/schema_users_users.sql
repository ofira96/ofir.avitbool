create table users
(
   	username varchar(100) not null,
	userId int not null,
	Email    varchar(256) not null,
	Password varchar(20)  not null,
	PRIMARY KEY(userId,Email)
);


INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('Byron Fields',1, 'Byro1324@walla.com', 'qa123');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('George Edwards',2,'hhh@gmail.com', '1a97');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('Rachel Howell',3, 'Howell@gmail.com', '23569');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('Lindsay Ferguson',4, 'Lindsrguson@walla.com', 'e34e');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('Michael Lawson',5, 'MichaelLawson@gmail.com', '1234r');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('Tobias Funke',6, 'Tobias11@gmail.com', 'wqsq');

select userId from users;