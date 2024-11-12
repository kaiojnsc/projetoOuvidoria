#Projeto Ouvidoria

def main():
    opcao = 0
    manifestacoes = []
    tiposManifestacao = {
        1: "Reclamação",
        2: "Elogio",
        3: "Sugestação"
    }

    while opcao != "7":
        print("Seja bem-vindo ao sistema de ouvidorias da Unifacisa!\n")
        print("1) Listagem das Manifestações")
        print("2) Listagem de Manifestações por Tipo")
        print("3) Criar uma nova manifestação")
        print("4) Exibir quantidade de manifestações")
        print("5) Pesquisar uma manifestação por código")
        print("6) Excluir uma manifestação por código")
        print("7) Sair do sistema\n")

        opcao = input("Digite a sua opção: ")

        if opcao == "1":
            print("\n1) Listagem das Manifestações\n")

            if len(manifestacoes) > 0:
                for i in range(len(manifestacoes)):
                    manifestacao = manifestacoes[i]

                    print("Código:", i + 1)
                    print("Conteúdo:", manifestacao["conteudo"])
                    print("Tipo:", manifestacao["tipo"], "\n")
            else:
                print("Não há manifestações disponíveis no momento!\n")

            opcao = goBackToMenu()
        elif opcao == "2":
            print("\n2) Listagem das Manifestações por Tipo\n")

            print("Qual tipo de manifestação você deseja listar?")
            print("1) Reclamação")
            print("2) Elogio")
            print("3) Sugestão\n")

            codigoTipoManifestacao = 0
            while codigoTipoManifestacao not in [1, 2, 3]:
                codigoTipoManifestacao = getPositiveInt("Digite o tipo a ser listado (1, 2 ou 3): ")

                if codigoTipoManifestacao not in [1, 2, 3]:
                    print("Opção inválida")

            print()

            manifestacoesPorTipo = []
            for i in range(len(manifestacoes)):
                manifestacao = manifestacoes[i]

                if manifestacao["tipo"] == tiposManifestacao[codigoTipoManifestacao]:
                    print("Código:", i + 1)
                    print("Conteúdo:", manifestacao["conteudo"])
                    print("Tipo:", manifestacao["tipo"], "\n")

                    manifestacoesPorTipo.append(manifestacao)

            if len(manifestacoesPorTipo) <= 0:
                print("A lista de", tiposManifestacao[codigoTipoManifestacao], "está vazia!\n",)

            opcao = goBackToMenu()
        elif opcao == "3":
            print("\n3) Criar uma nova manifestação\n")

            adicionarNovaManifestacao = "s"
            while adicionarNovaManifestacao == "s":
                print("Qual o tipo da sua manifestação?")
                print("1) Reclamação")
                print("2) Elogio")
                print("3) Sugestão\n")

                codigoTipoManifestacao = 0
                while codigoTipoManifestacao not in [1, 2, 3]:
                    codigoTipoManifestacao = getPositiveInt("Digite o tipo da manifestação (1, 2 ou 3): ")

                    if codigoTipoManifestacao not in [1, 2, 3]:
                        print("Opção inválida")

                conteudoManifestacao = ""
                while len(conteudoManifestacao) <= 0:
                    conteudoManifestacao = input("Digite o conteúdo da manifestação: ").strip()

                    if len(conteudoManifestacao) > 0:
                        manifestacoes.append({
                            "conteudo": conteudoManifestacao,
                            "tipo": tiposManifestacao[codigoTipoManifestacao],
                        })
                        print("\nManifestação adicionada com sucesso!\n")
                    else:
                        print("O conteúdo da manifestação é obrigatório!")

                adicionarNovaManifestacao = ""
                while adicionarNovaManifestacao not in ["s", "n"]:
                    adicionarNovaManifestacao = input("Você deseja adicionar uma nova manifestação? (s/n) ").strip().lower()

                    if adicionarNovaManifestacao not in ["s", "n"]:
                        print("Opção inválida")
                print()
        elif opcao == "4":
            print("\n4) Exibir quantidade de manifestações\n")

            print("Existem", len(manifestacoes), "manifestações cadastradas no sistema!\n")

            opcao = goBackToMenu()
        elif opcao == "5":
            print("\n5) Pesquisar uma manifestação por código\n")

            codigoManifestacao = getPositiveInt("Digite o código da manifestação desejada: ")

            if codigoManifestacao > 0 and codigoManifestacao <= len(manifestacoes):
                manifestacaoPesquisada = manifestacoes[codigoManifestacao - 1]

                print("\nCódigo:", codigoManifestacao)
                print("Conteúdo:", manifestacaoPesquisada["conteudo"])
                print("Tipo:", manifestacaoPesquisada["tipo"], "\n")
            else:
                print("Essa manifestação não está cadastrada no sistema!\n")

            opcao = goBackToMenu()
        elif opcao == "6":
            print("\n6) Excluir uma Manifestação pelo Código\n")

            if len(manifestacoes) > 0:
                confirmarDelecao = "n"

                while confirmarDelecao != "s":
                    codigoManifestacao = getPositiveInt("Digite o código da manifestação a ser excluída: ")

                    if codigoManifestacao > 0 and codigoManifestacao <= len(manifestacoes):
                        manifestacao = manifestacoes[codigoManifestacao - 1]

                        print("\nCódigo:", codigoManifestacao)
                        print("Conteúdo:", manifestacao["conteudo"])
                        print("Tipo:", manifestacao["tipo"], "\n")

                        confirmarDelecao = ""
                        while confirmarDelecao not in [ "s", "n"]:
                            confirmarDelecao = (
                                input("Essa é a manifestação que você quer excluir? (s/n) ")
                                .strip()
                                .lower()
                            )
                            print()

                            if confirmarDelecao not in [ "s", "n"]:
                                print("Opção inválida")

                        if confirmarDelecao == "s":
                            manifestacoes.pop(codigoManifestacao - 1)
                            print("Manifestação deletada com sucesso!\n")
                    else:
                        print("\nManifestação não encontrada!\n")
                        confirmarDelecao = "s"

            else:
                print("Não há manifestações disponíveis para remoção\n")

            opcao = goBackToMenu()
        elif opcao != "7":
            print("Opção inválida\n")

    print("\nObrigado por utilizar o programa! Volte sempre!")


def goBackToMenu():
    return input("Aperte qualquer tecla para voltar ao menu\nou digite 7 para encerrar o programa\n")


def getPositiveInt(message: str):
    """Return a valid positive integer input"""

    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")


try:
    main()
except KeyboardInterrupt:
    print("\nObrigado por utilizar o programa! Volte sempre!")
