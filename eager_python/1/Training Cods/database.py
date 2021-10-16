import sqlite3
def main():
    db=sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    db.execute('DROP TABLE IF EXISTS test')
    db.execute('CREATE TABLE test(t1 text, i1 int)')
    db.execute('INSERT INTO test(t1 , i1) value(? ,?)' , ('one',1))
    db.execute('INSERT INTO test(t1 , i1) value(? ,?)' , ('two',2))
    db.execute('INSERT INTO test(t1 , i1) value(? ,?)' , ('three',3))
    db.execute('INSERT INTO test(t1 , i1) value(? ,?)' , ('four',4))
    db.execute('INSERT INTO test(t1 , i1) value(? ,?)' , ('five',5))

    db.commit()

    cursor = db.execute('SELECT FORM testORDER BY t1')
    for row in cursor: print(row)
if __name__ == '__main__':
    main()
