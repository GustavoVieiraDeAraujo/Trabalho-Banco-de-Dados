CREATE TABLE clubs(
	team_id INTEGER PRIMARY KEY,
	shortName VARCHAR(100),
	fullName VARCHAR(200),
	imageURL TEXT,
	city VARCHAR(100),
	country VARCHAR(100),
	website VARCHAR(200),
	dateOfFoundation DATE,
	members NUMERIC,
	marketValue MONEY,
	squadSize INTEGER,
    	squadAvarageAge NUMERIC,
    	squadForeigners INTEGER,
    	squadNationalTeamPlayers INTEGER,
    	stadiumName VARCHAR(200),
    	stadiumSeats INTEGER,
    	competition VARCHAR(10)
);
