def calculo_potencia(expoente):
    def potencia(base):
        return base ** expoente
    return potencia

def main():
    base_expoente = input("Digite a base e o expoente separados por espaço: ")
    base, expoente = (int(i) for i in base_expoente.split())
    potencia_de = calculo_potencia(expoente)
    res_potencia = potencia_de(base)
    print(f"{base} elevado a {expoente} = {res_potencia}")

if __name__ == "__main__":
        main()