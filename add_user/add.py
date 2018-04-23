import psycopg2
try:
    conn = psycopg2.connect("dbname='lab_database' user='admin' host='localhost' password='qwerty12345'")
    cur = conn.cursor()
except:
    print "fuck"
user = open("user.txt", 'r')
users = list()
for line in user:
    s = line[:len(line)-1]
    users.append(s.split(' '))
user.close()

nik = open("nik.txt", 'r')
niks = list()
for i in nik:
    niks.append(i[:len(i)-1])
nik.close()

for i in xrange(len(niks)):
    cur.execute("""insert into users(username, first_name, second_name, password, group_id)
                    values('{0}', '{1}', '{2}', '{3}', '{4}')""".format(niks[i], users[i][1], users[i][0], niks[i], 2))

conn.commit()
cur.close()
conn.close()
