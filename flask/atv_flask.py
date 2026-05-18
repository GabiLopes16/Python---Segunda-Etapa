from flask import Flask

app = Flask(__name__) 

@app.route('/decorator')
def atv_pyton():
  return 'Olá Janaina! Um decorator em Python é uma função especial que modifica ou estende o comportamento de outra função, método ou classe sem alterar o código original. Eles servem para reutilizar lógica em múltiplas funções, tornando o código mais organizado, legível e seguindo o princípio DRY Dont Repeat Yourself - Não Repita a Si Mesmo. No Flask, o decorator @app.route é usado para mapear uma URL específica a uma função Python (view function). Quando o usuário acessa essa URL no navegador, o Flask executa a função decorada.'

if __name__ == '__main__':
  app.run(debug=True)