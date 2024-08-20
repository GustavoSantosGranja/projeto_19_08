from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica

def main():
    lista_pf = []

    while True:
        opcao = int(input("Escolha uma Opção: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair: "))

        if opcao == 1:
            while True: 
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 0 - Voltar ao menu anterior: "))
                # Cadastro
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o Nome da Pessoa Fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento  = float(input("Digite o rendimento mensal (somente números): "))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade  = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("Tem mais de 18 anos.")
                    else: 
                        print("A pessoa tem menos de 18 anos: Retorne ao Menu...")
                        continue

                    novo_end_pf.logradouro =  input("Digite o Logradouro: ")
                    novo_end_pf.numero = input("Digite o Número: ")

                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pf.endereco_Comercial  = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!")

                # Listar pessoa física
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Data de Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto: R$ {cada_pf.calcular_imposto(cada_pf.rendimento):.2f}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break 

                else: 
                    print("Opção inválida, por favor digite uma das opções abaixo indicadas.")
        elif opcao == 2:
            print("Funcionalidades para pessoa jurídica não implementadas.")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema!")
            break

        else: 
            print("Opção Inválida, por favor digite uma das opções válidas.")

if __name__ == "__main__":
    main()  # Chama a função principal
