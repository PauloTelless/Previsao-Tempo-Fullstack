import requests
from flask import Flask, request, render_template

app = Flask(__name__)

def formatar_nome_cidade(nome_cidade):
    palavras = nome_cidade.split()
    nome_formatado = ' '.join(word.capitalize() for word in palavras) ###Função criada para cidades com nomes compostos. Quando o usuário coloca o nome, a cada espaço, a letra fica maiúscula para se adequar à gramática###
    return nome_formatado

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/previsao', methods=['POST'])
def get_previsao():
    cidade = request.form.get('cidade')
    cidade_formatada = formatar_nome_cidade(cidade)
    
    API_Key = ''
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade_formatada}&appid={API_Key}&lang=pt_br'
    
    try:
        info = requests.get(link).json()
        temperatura = int(info['main']['temp']) - 273
        ceu = str(info['weather'][0]['description']).capitalize()
        umidade = info['main']['humidity']
        velocidade_vento = int(info['wind']['speed']) * 3.6
        
    except KeyError:
            return render_template('error.html')
        
    return render_template('previsao.html', cidade=cidade_formatada, temperatura=temperatura, umidade=umidade, velocidade_vento=velocidade_vento, ceu=ceu)

if __name__ == '__main__':
    app.run(debug=True)
    