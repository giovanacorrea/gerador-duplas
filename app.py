from flask import Flask, render_template, request
import random
import itertools

app = Flask(__name__)


def pares(lista):
    # Gera todos os pares possíveis usando combinations
    todos_pares = list(itertools.combinations(lista, 2))
    
    # Embaralha os pares para garantir que a ordem seja aleatória
    random.shuffle(todos_pares)

    # Lista para armazenar os pares finais
    pares_final = []
    
    # Variável para armazenar o último par
    ultimo_par = None
    
    while todos_pares:
        # Tenta encontrar um par que não repita nenhum elemento do último par
        for i, par in enumerate(todos_pares):
            if not ultimo_par or (par[0] not in ultimo_par and par[1] not in ultimo_par):
                pares_final.append(par)
                ultimo_par = par
                todos_pares.pop(i)
                break
        else:
            # Se não encontrar, reseta o último par para permitir novos pares
            ultimo_par = None

    return pares_final


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_jogadores = int(request.form.get('qtdjogadores'))
        jogadores = [request.form.get(f'player-{i}') for i in range(1, num_jogadores + 1)]
        novospares = pares(jogadores)
        return render_template('resultado.html', pares=novospares)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
