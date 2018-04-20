import sqlite3

con=sqlite3.connect("../:memory")
cur=con.cursor()

create_str="""
CREATE TABLE address(
id serial,
postcode text,
prefecture text,
street text);
"""

#cur.execute(create_str)

insert_str="""
INSERT INTO address(postcode, prefecture, street)
VALUES(?, ?, ?);
"""
info = ('100', 'Tokyo', 'Chiyodaku')
cur.execute(insert_str,info)

con.commit()

select_str="""
SELECT id, prefecture, street FROM address;
"""
cur.execute(select_str)
print("------------ SELECT -----------")
for x in cur:
    print(x)
print("-------------------------------")

delete_str="""
DELETE FROM address;
"""
cur.execute(delete_str)
con.commit()

select_str = """
SELECT id, prefecture, street FROM address
"""
cur.execute(select_str)

print("------------ DELETE -----------")
for x in cur:
    print(x)
print("-------------------------------")