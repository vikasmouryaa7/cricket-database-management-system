--Cricket database management system
--vikas

--DDL statements for building the database
create table team(Tid int not null, Tname varchar(50), ShortN varchar(10), coach varchar(25), Field_bat varchar(8), Trophy_won int, primary key(Tid));

create table game(gid int not null, date datetime, toss varchar(25), result varchar(25), player_of_match varchar(25), tid int, primary key(gid), foreign key(tid) references team(tid));

create table player(pid int not null, fname varchar(15), lname varchar(15), dob datetime, nationality varchar(25), type varchar(20), tid int, primary key(pid), foreign key(tid) references team(tid), jersey_no int);

create table participates(pid int, gid int, foreign key(gid) references game(gid), foreign key(pid) references player(pid));

show tables;

--Populating the Database
--other values are inserted using the frontend
insert into team values(1, 'India', 'ind', 'Rahul Dravid', 'batting', 9)

insert into game values(3,'2020-11-10','Australia', 'India', 'Virat Kohli', 1);

insert into player values(9, 'Rohit', 'Sharma', '1987-04-30', 'Indian', 'Batsman', 1, 45);

insert into participates values(9,1);

--Join Queries
--To find all players and team info of players who play for ‘India’:  (Natural Join)
select * from player natural join team;

--Details of all teams even though they don’t have players: (Right outer join)
select pid,fname,lname,team.tid,tname from player right join team on player.tid=team.tid;

--Details of all the players even though they are not participating in a given game: (Left outer join)
select * from player left join participates on player.pid=participates.pid;

--Details of all the players and teams without losing information of any team or player: (Full outer join)
select pid,fname,lname,team.tid,tname from player right join team on player.tid=team.tid union select pid,fname,lname,team.tid,tname from player left join team on team.tid=player.tid;

--Aggregate Functions
--Count of games where the result was in India’s favor:
select count(result) from game where result='India';

--Finding maximum and minimum jersey number among all the players:
select max(jersey_no), min(jersey_no) from player;

--Counting the number of batsmen in the Indian team:
select count(type) from player where type = 'Batsman' and nationality = 'India';

--Most recent match where ‘Virat Kohli’ was the player of the match:
select max(date) from game where player_of_match = 'Virat Kohli';

--Set Operations
--Team id’s of all the teams that have or have not played atleast one game
select tid from team union select tid from game;

--Team id’s of all the teams that have played atleast one game
select tid from team intersect select tid from game;

--Players that participate or do not participate in a given game
select pid from player union select pid from participates; 

--Players that participate in a given game
select pid from player intersect select pid from participates; 

--Functions and Procedures
--FUNCTION
--Depending on the trophies won, tells about the performance of the team
DELIMITER $$
CREATE FUNCTION player_performance(trophy_won int)
RETURNS VARCHAR(25)
DETERMINISTIC 
	BEGIN
		DECLARE performance_msg VARCHAR(50);
		IF trophy_won > 3 THEN 
			SET performance_msg = "Good performance";  
		ELSEIF trophy_won > 1 THEN 
			SET performance_msg = "Average performance";
		ELSE 
			SET performance_msg= "Bad performance"; 
		END IF;
		RETURN performance_msg;	
	END; $$ 
DELIMITER ;
--Executing function
SELECT tid,tname,trophy_won,player_performance(trophy_won) FROM team;

--PROCEDURE
--Checking if a player participates in at least one game or not
DELIMITER $$
CREATE procedure player_participates(
IN pid int, OUT msg varchar(30))
BEGIN
DECLARE cnt int;
set cnt = (SELECT count(pid) from participates group by pid);
IF cnt < 1 THEN
   set msg= "Player doesn't participate in a single game";
ELSE
   set msg = (select pid from participates where cnt >= 1);  
END IF;
END;$$
DELIMITER ;

--calling procedure
call player_participates(1, @result);
select @result;

--Triggers and Cursors
--TRIGGER
--Trigger for when a user tries to update the player with to a jersey number is 0
DELIMITER $$
CREATE TRIGGER before_update_player
BEFORE UPDATE  
ON player FOR EACH ROW  
BEGIN  
    DECLARE error_msg VARCHAR(255);  
    SET error_msg = ('The jersey number cannot be changed to 0');  
    IF new.jersey_no = 0 THEN  
    SIGNAL SQLSTATE '45000'  
    SET MESSAGE_TEXT = error_msg;  
    END IF;  
END $$  
DELIMITER ;

--triggered
Update player set jersey_no = 0 where pid = 1;

--CURSOR
--used in frontend (in database.py file)
c = mydb.cursor()











