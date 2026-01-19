nomeHeroi = "Aragorn"
moedasOuro = 500
pontosVida = 150

inventario = ["Espada", "Escudo", "Poção"]

monstro = {
    "nome": "Dragão Negro",
    "tipo": "fogo",
    "nivel": 25
}

guilda = [
    {
        "nome": "Aragorn",
        "classe": "Guerreiro",
        "nivel": 20
    },
    {
        "nome": "Legolas",
        "classe": "Arqueiro",
        "nivel": 18
    },
    {
        "nome": "Gandalf",
        "classe": "Mago",
        "nivel": 30
    }
]

inventario.append("Mapa")
moedasOuro -= 10

print("=== HERÓIS DA GUILDA ===")
for heroi in guilda:
    print(f"Nome: {heroi['nome']}")

print("\n=== RESUMO DO HERÓI ===")
print(f"Herói: {nomeHeroi}")
print(f"Moedas de Ouro: {moedasOuro}")
print(f"Pontos de Vida: {pontosVida}")
print(f"Inventário: {inventario}")
print(f"\nMonstro Enfrentado: {monstro['nome']} ({monstro['tipo']}) - Nível {monstro['nivel']}")