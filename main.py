from funcoes import (
    eh_primo,
    mdc,
    euclides_estendido,
    inverso_modular,
    totiente_euler,
    pot_mod,
    congruencia_linear,
    teoremaChinesResto,
)

def exibir_menu():
    print("[1] Verificar se número é Primo")
    print("[2] Calcular MDC")
    print("[3] Algoritmo de Euclides Estendido")
    print("[4] Calcular Inverso Modular")
    print("[5] Função Totiente de Euler (Phi)")
    print("[6] Exponenciação Modular")
    print("[7] Resolver Congruência Linear")
    print("[8] Teorema Chinês do Resto")
    print("[0] Sair")
    print("="*40)

def main():
    while True:
        exibir_menu()
        opcao = input("Qual função tu quer executar? ").strip()

        if opcao == "0":
            print("\nEncerrando o programa.")
            break

        elif opcao == "1":
            print("\n--- VERIFICAR SE É PRIMO ---")
            n = int(input("Digite o número: "))
            print(f"Resultado: {'É PRIMO' if eh_primo(n) else 'NÃO É PRIMO'}")

        elif opcao == "2":
            print("\n--- CALCULAR MDC ---")
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            print(f"Resultado: MDC({a}, {b}) = {mdc(a, b)}")

        elif opcao == "3":
            print("\n--- EUCLIDES ESTENDIDO ---")
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            mdc_val, x, y = euclides_estendido(a, b)
            print(f"Resultado: MDC = {mdc_val} | x = {x} | y = {y}")

        elif opcao == "4":
            print("\n--- INVERSO MODULAR ---")
            a = int(input("Digite a base (a): "))
            m = int(input("Digite o módulo (m): "))
            try:
                print(f"Resultado: Inverso de {a} mod {m} é {inverso_modular(a, m)}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "5":
            print("\n--- FUNÇÃO TOTIENTE DE EULER ---")
            n = int(input("Digite o número (n): "))
            print(f"Resultado: Phi({n}) = {totiente_euler(n)}")

        elif opcao == "6":
            print("\n--- EXPONENCIAÇÃO MODULAR ---")
            base = int(input("Digite a base: "))
            exp = int(input("Digite o expoente: "))
            m = int(input("Digite o módulo: "))
            print(f"Resultado: {base}^{exp} mod {m} = {pot_mod(base, exp, m)}")

        elif opcao == "7":
            print("\n--- CONGRUÊNCIA LINEAR ---")
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            m = int(input("Digite o módulo m: "))
            solucoes = congruencia_linear(a, b, m)
            print(f"Resultado: Soluções: {solucoes}" if solucoes else "Sem soluções")

        elif opcao == "8":
            print("\n--- TEOREMA CHINÊS DO RESTO ---")
            restos_in = input("Digite tres restos (separados por vírgula): ")
            modulos_in = input("Digite tres módulos (separados por vírgula): ")
            
            restos = [int(x.strip()) for x in restos_in.split(",")]
            modulos = [int(x.strip()) for x in modulos_in.split(",")]
            
            try:
                print(f"Resultado: Menor X é {teoremaChinesResto(restos, modulos)}")
            except Exception as e:
                print(f"Erro: {e}")
        
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()
