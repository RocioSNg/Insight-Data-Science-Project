
# create table containing information for tumblr artists #

DROP TABLE IF EXISTS Artists;
CREATE TABLE Artists(Id INT PRIMARY KEY AUTO_INCREMENT,
	Blog_Name VARCHAR(255) not null UNIQUE, 
	Blog_url text,
	Posts_Count INT);

-- INSERT INTO Artists(Blog_Name) VALUES('crowdedteeth');

SELECT * FROM Artists;

