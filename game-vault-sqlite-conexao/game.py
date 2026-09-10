import os #Biblioteca para habilitar cmd's terminal
import sqlite3 #Banco de dados

# Variável com o nome do BD a ser criado
CAMINHO_BANCO = "jogos.db"

def exibir_cabecalho(texto):
    os.system('cls') # Limpa a tela

    # Cria um efeito visual na palavra "GameVault"
    linha ="*" *len(texto)
    print(linha)
    print(texto)
    print(linha)
    print() #Linha em branco

exibir_cabecalho("GameVault")

def inicializar_banco():
    # Abre a conexão com o banco de dados (o indicado em: "CAMINHO_BANCO" no caso: "jogos.db")
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Diz ao BD que de fato SQL está habilitado
    cursor = conn.cursor()

    #
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        plataforma TEXT NOT NULL,
        zerado BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )


    #
    conn.commit()
    #Fecha a conexão
    conn.close()

# chamando a função
inicializar_banco()


def listar_jogos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")

    #"fetchall" - Devolve TODAS as linhas do resultado como Tupla
    jogos = cursor.fetchall()

    conn.close()

    # se BD vazio mostra a mensagem abaixo
    if not jogos:
        print("Nenhum jogo cadastrado ainda")