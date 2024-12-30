CREATE TABLE referees(
	referee_id INTEGER PRIMARY KEY,
	shortName VARCHAR(100),
	fullName VARCHAR(200), 
	dateOfBirth DATE,
	age INT,
	countryOfBirth VARCHAR(100),
	joinedLeague DATE,
	imageURL TEXT
);