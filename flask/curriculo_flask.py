from flask import Flask

app = Flask(__name__) 

@app.route('/curriculo')
def home():
   return'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curriculo</title>
</head>
<body>
    <h1>Curriculo</h1>
    
    <h2>Informações Pessoais</h2>
    <ul></ul>
    <strong>Gabrele Lopes</strong>
    <li><strong>Email:</strong>gabrielelopesleite@gmail.com.br</li>
    <li><strong>Telefone:</strong>(31) 989506615</li></ul>
    <ul>

        <h2>Cursos extracurriculares</h2>
         <li><strong>Introdução a Cibersegurança - </strong>certificado em conclusão</li>
         <li><strong>Introdução a loT e transformação digital - </strong>certificado em conclusão</li>
         <li><strong>Introdução a IA moderna - </strong>certificado em conclusão</li>
    </ul>
    <h2>Habilidades Tecnicas</h2>
    <ul>
    <li>HTML e CSS3</li>
    <li>JavScript</li>
    <li>MySQL</li>
    <li>Python</li>
    <li>PHP</li>
 </ul>
 <h2>Competências Pessoais</h2>
 <ul>
    <h2>Habilidades Tecnicas</h2>
    <li>Comunicação e proativade</li>
    <li>Orgaização e responsabilidade</li>
    <li>Facilidade em trabalhar em equipe</li>
    <li>Foco em resultados e aprendizado rápido</li>
 </ul>
 <h2>Idiomas</h2>
 <li>Inglês intermediário</li>
</body>
</html>
'''

if __name__ == "__main__":
  app.run(debug=True)