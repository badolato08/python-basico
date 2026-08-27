# Digitar (Aqui)

# Texto especial para usar no projeto (abaixo)
# 𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤

# Sabor Express - Versão Orientada a Objetos
# Sistema de cadastro e gerenciamento de restaurantes

import os


# Classe que representa um único restaurante cadastrado no sistema.
# Cada objeto dessa classe guarda seus próprios dados
# (nome, categoria, ativo).

class Restaurante:

    # Construtor: roda automaticamente quando um novo Restaurante é criado.
    # Recebe nome e categoria, e já define ativo como False por padrão.

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False  # Todos os restaurantes começam inativos

    # Método que inverte o estado do restaurante (ativo <-> inativo).
    # Não recebe parâmetros além de self porque só mexe nos próprios dados.

    def alternar_estado(self):
        self.ativo = not self.ativo

    # Método especial: define como o objeto aparece quando usado em
    # print(restaurante) ou dentro de uma f-string.

    def __str__(self):
        status = "ativado" if self.ativo else "desativado"
        return f"-{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {status}"


# Classe principal do sistema.
# Guarda a lista de restaurantes e concentra as regras de negócio:
# cadastrar, buscar e listar.

class SaborExpress:

    # Construtor: cria a lista de restaurantes já com alguns itens iniciais.

    def __init__(self):
        self.restaurantes = [
            Restaurante("Praça", "Japonesa"),
            Restaurante("Pizza Suprema", "Pizza"),
            Restaurante("Cantina", "Italiano"),
        ]

    # Cria um novo objeto Restaurante e adiciona na lista interna.

    def cadastrar_restaurante(self, nome, categoria):
        novo_restaurante = Restaurante(nome, categoria)
        self.restaurantes.append(novo_restaurante)
        return novo_restaurante

    # Percorre a lista de restaurantes cadastrados.
    # Retorna o objeto restaurante se achar, ou None se não encontrar.

    def buscar_restaurante(self, nome):
        for restaurante in self.restaurantes:
            if restaurante.nome == nome:
                return restaurante
        return None

    # Retorna a lista de restaurantes cadastrados.
    #A formação da exibição é responsabilizada da classe Menu
    def listar_restaurantes(self):
        return self.restaurantes


# Classe responsável por toda a interação com o usuário: exibir textos
# ler as opções digitadas e chamar os métodos do SaborExpress.

class Menu:

    # Construtor: cria um SaborExpress para o Menu poder operar sobre ele.

    def __init__(self):
        self.app = SaborExpress()

    # ---------- Métodos de exibição ----------

    # Limpa a tela e mostra um subtítulo formatado com asteriscos em volta.

    def exibir_subtitulo(self, texto):
        os.system("cls")  # Limpa a tela no Windows
        linha = "*" * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

    # Mostra o nome estilizado do programa na tela.
    def exibir_nome_do_programa(self):
        print(
            """
        𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤
        """
        )

    # Mostra as opções do menu principal para o usuário escolher.
    def exibir_opcoes(self):
        print("1. Cadastrar restaurante")
        print("2. Listar restaurantes")
        print("3. Alternar estado do restaurante")
        print("4. Sair\n")

    # ---------- Métodos de ação(chama a partir do menu) ----------

    # Pede nome e categoria ao usuário e manda o SaborExpress cadastrar.

    def cadastrar_novo_restaurante(self):
        self.exibir_subtitulo("Cadastro de novos restaurantes\n")
        nome = input(f"Digite o nome do restaurante que deseja cadastrar: ")
        categoria = input(
            f"Digite o nome da categoria do restaurante {nome}: ")

        self.app.cadastrar_restaurante(nome, categoria)
        print(f"O restaurante {nome} foi cadastrado com sucesso!")

        self.voltar_ao_menu_principal()

    # Pede o nome de um restaurante e alterna seu estado(ativo/inativo).
    def alternar_estado_do_restaurante(self):
        self.exibir_subtitulo("Alternando estado do restaurante\n")
        nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")

        restaurante = self.app.buscar_restaurante(nome_restaurante)

        # Só mexe no estado se o restaurante realmente foi encontrado.

        if restaurante:
            restaurante.alternar_estado()
            status = "ativado" if restaurante.ativo else "desativado"
            print(f"O restaurante {nome_restaurante} foi "
                f"{status} com sucesso!"
            )

        else:
            print("O restaurante não foi encontrado!")

        self.voltar_ao_menu_principal()

    # Lista todos os restaurantes cadastrados, um por linha.
    def listar_restaurantes(self):
        self.exibir_subtitulo("Listando os restaurantes\n")

        print(f"{'nome_restaurante'.ljust(21)} | {'categoria'.ljust(20)} | status")

        # print(restaurante) usa o __str__ definido na classe Restaurante,
        #não precisa formatara linha manualmente de novo
        for restaurante in self.app.listar_restaurantes():
            print(restaurante)

        self.voltar_ao_menu_principal()

    # Encerra o aplicativo mostrando uma mensagem de despedida.
    def finalizar_app(self):
        self.exibir_subtitulo("Finalizando o app\n")

    # Mostra mensagem de opção inválida e volta ao menu principal.
    def opcao_invalida(self):
        print("Opção inválida!\n")
        self.voltar_ao_menu_principal()

    # Pausa a execução esperando o usuário apertar uma tecla,
    # depois chama main() de novo para reiniciar o ciclo do menu.
    def voltar_ao_menu_principal(self):
        input("\nDigite uma tecla para voltar ao menu principal")
        self.main()

    # Lê a opção digitada e decide qual método chamar.
    # Usa try/except para tratar o caso de o usuário digitar algo não numérico.
    def escolher_opcao(self):
        try:
            opcao_escolhida = int( input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                self.cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                self.listar_restaurantes()
            elif opcao_escolhida == 3:
                self.alternar_estado_do_restaurante()
            elif opcao_escolhida == 4:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:

            # Captura erro de conversão para int() (texto não numérico)
            self.opcao_invalida()

    # Função principal: limpa a tela, mostra o nome do programa,
    # as opções e processa a escolha do usuário.
    def main(self):
        os.system("cls")
        self.exibir_nome_do_programa()
        self.exibir_opcoes()
        self.escolher_opcao()


# Ponto de entrada do programa:
# só roda o menu se o arquivo for executado diretamente.
if __name__ == "__main__":
    menu = Menu()
    menu.main()
