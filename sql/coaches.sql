CREATE TABLE coaches(
	coach_id INTEGER PRIMARY KEY,
	shortName VARCHAR(100),
	fullName VARCHAR(200),
	imageURL TEXT,
	dateOfBirth DATE,
	age INT,
	cityOfBirth VARCHAR(100),
	countryOfBirth VARCHAR(100),
	club INTEGER,
	joinedClub DATE,
	contractExpires DATE
);