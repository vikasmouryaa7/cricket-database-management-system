import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pes1ug20cs274_project"
)
c = mydb.cursor()
 
 
def create_table1():
    c.execute('CREATE TABLE IF NOT EXISTS team(Tid int not null, Tname varchar(50), ShortN varchar(10), coach varchar(25), Field_bat varchar(8), Trophy_won int, primary key(Tid));')

def create_table2():
    c.execute('CREATE TABLE IF NOT EXISTS game(gid int not null, date datetime, toss varchar(25), result varchar(25), player_of_match varchar(25), tid int, primary key(gid), foreign key(tid) references team(tid));')

def create_table3():
    c.execute('CREATE TABLE IF NOT EXISTS player(pid int not null, fname varchar(15), lname varchar(15), dob datetime, nationality varchar(25), type varchar(20), tid int, primary key(pid), foreign key(tid) references team(tid), jersey_no int);')

def create_table4():
    c.execute('CREATE TABLE IF NOT EXISTS participates(pid int, gid int, foreign key(gid) references game(gid), foreign key(pid) references player(pid));')
 
def add_data1(pid,fname,lname,dob,nationality,type,tid,jersey_no):
    c.execute('INSERT INTO Player (pid,fname,lname,dob,nationality,type,tid,jersey_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (pid,fname,lname,dob,nationality,type,tid,jersey_no))
    mydb.commit()

def add_data2(gid,date,toss,result,player_of_match,tid):
    c.execute('INSERT INTO Games (gid,date,toss,result,player_of_match,tid) VALUES (%s,%s,%s,%s,%s,%s);',
              (gid,date,toss,result,player_of_match,tid))
    mydb.commit()

def add_data3(tid,Tname,ShortN,coach,Field_bat,Tropy_won):
    c.execute('INSERT INTO Team (tid,Tname,ShortN,coach,Field_bat,Tropy_won) VALUES (%s,%s,%s,%s,%s,%s);',
              (tid,Tname,ShortN,coach,Field_bat,Tropy_won))
    mydb.commit()

def add_data4(pid,gid):
    c.execute('INSERT INTO participates (pid,gid) VALUES (%s,%s);',
              (pid,gid))
    mydb.commit()
 
def query0(text):
    c.execute(text)
    data = c.fetchall()
    return data
 
def view_all_data1():
    c.execute('SELECT * FROM player')
    data = c.fetchall()
    return data
    
def view_all_data2():
    c.execute('SELECT * FROM game')
    data = c.fetchall()
    return data
    
def view_all_data3():
    c.execute('SELECT * FROM Team')
    data = c.fetchall()
    return data
    
def view_all_data4():
    c.execute('SELECT * FROM participates')
    data = c.fetchall()
    return data
 
 
def get_details1(player_name):
    c.execute('SELECT * FROM Player WHERE pid="{}"'.format(player_name))
    data = c.fetchall()
    return data
    
def get_details2(team_name):
    c.execute('SELECT * FROM team WHERE tid="{}"'.format(team_name))
    data = c.fetchall()
    return data
   
def edit_details1(pid,new_jersey_no):
    c.execute("UPDATE player SET jersey_no=%s WHERE pid=%s", (new_jersey_no,pid))
    mydb.commit()
    data = c.fetchall()
    return data
    
def edit_details2(tid,new_coach):
    c.execute("UPDATE team SET coach=%s WHERE tid=%s", (new_coach,tid))
    mydb.commit()
    data = c.fetchall()
    return data
    
def delete_data(player_name):
    c.execute('DELETE FROM player WHERE pid="{}"'.format(player_name))
    mydb.commit()