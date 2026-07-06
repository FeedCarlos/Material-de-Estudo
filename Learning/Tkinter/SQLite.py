# Criar o banco de dados e conexão
import sqlite3
con = sqlite3.connect("cinema.db")

# Criar um objeto cursor
cur = con.cursor()

# Criar uma tabela 
#cur.execute("CREATE TABLE filme(titulo, ano, duracao)")

# Verificar se tabela foi criada
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

# Inserir linha na tabela
cur.execute("""
    INSERT INTO filme VALUES
        ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 178),
        ('Conan, o Bárbaro', 1982, 129)    
""")
con.commit()

# Verificar se dados foram inseridos corretamente
res = cur.execute("SELECT titulo FROM filme")
res.fetchall()

# Inserir mais registros
dados_filmes = [
    ("Indiana Jones e a Última Cruzada", 1989, 127),
    ("O Nome da Rosa", 1986, 126),
    ("Deus e o Diabo na Terra do Sol", 1964, 120),
    ("De volta para o Futuro", 1985, 116)
]

# Usamos placeholders para vilcular valores no Python a declarações SQL, para evitar ataques
# Cada placeholder representa uma coluna
cur.executemany("INSERT INTO filme (titulo, ano, duracao) VALUES(?, ?, ?)", dados_filmes)
# opcionalmente, sem informar os nome das colunas:
# cur.executemany("INSERT INTO filme VALUES(?, ?, ?), dados_filmes")
con.commit()

# verificar
res = cur.execute("SELECT titulo FROM filme")
res.fetchall()

for linha in cur.execute("SELECT ano, titulo FROM filme ORDER BY ano"):
    print(cur)

# Gerenciador de Contexto com objeto Connection: Dispensa commit ou rollback explícitos
try:
    with con:
        con.execute("INSERT INTO filme (titulo, ano, duracao) VALUES(?,?,?)", ("Oppenheimer", 2022))
except sqlite3.ProgrammingError:
    print("Banco de dados não acessível.")

res = cur.execute("SELECT titulo FROM filme")
res.fetchall()

# Fechar o banco de dados
con.close