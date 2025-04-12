
# perguntas_matematica.py

def perguntas_matematica():
    perguntas_respostas = {
        "Quanto é 5 + 3?": 5 + 3,
        "Quanto é 10 - 4?": 10 - 4,
        "Quanto é 6 * 7?": 6 * 7,
        "Quanto é 20 / 5?": 20 / 5,
        "Quanto é 2 ** 3?": 2 ** 3,
        "Quanto é 15 % 4?": 15 % 4,
        "Quanto é (3 + 2) * 4?": (3 + 2) * 4,
        "Quanto é 100 // 9?": 100 // 9,
        "Quanto é 9 ** 2?": 9 ** 2,
        "Quanto é (10 + 5) / (3 * 2)?": (10 + 5) / (3 * 2)
    }

    for pergunta, resposta in perguntas_respostas.items():
        print(f"{pergunta}\nResposta: {resposta}\n")

if __name__ == "__main__":
    perguntas_matematica()
