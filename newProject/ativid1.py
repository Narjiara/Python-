import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2023",
    database = "escola_turmac"
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)


nome1 = "rosa"
telefone1 = "67895432091"
turma1 = "C"
media1 = "7"
meucursor = banco.cursor()
sql = "insert into alunos (nome,telefone,turma,media) values (%s, %s,%s,%s)"
data = (nome1,telefone1,turma1,media1)
meucursor.execute(sql,data)
banco.commit()
userid = meucursor.lastrowid
print(userid)
meucursor.close()
banco.close()