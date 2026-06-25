# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Gabriele Lopes 
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

Os models 

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
streamflix.db, app.py.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

class ModeloBase = base.py / class FilmeFavorito = filme_favorito.py / class HistoricoBusca = historico_busca

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
Da classe ModeloBase, ganhando id, data criação e data atualizção
    

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

"filmes_favoritos", pela flexibilidade e padronização


**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id = db.Column(db.Integer, nullable=False, unique=True)


**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Ele salva/adiciona um novo registro no banco, caso exista a operação retorna "none", ou seja não faz nada 

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

@classmethod
    def ultimas(cls, limite=8):
        return cls.query.order_by(cls.data_criacao.desc()).limit(limite).all()

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
 
 Apenas alguns campos espelhados, id, ano, nota, título 

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
 
As classes, importa direto para organizar e simplificar o código
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

 3 Blueprints / Blueprint "dashboard" /  Blueprint "favoritos" url_prefix="/favoritos"/  Blueprint "filmes"  url_prefix="/filmes"

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

filmes_controller.py, a criação de uma rota = @filmes_bp.route("/populares") def populares():

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

busca a lista de filmes mais acessados através de uma API e recupera do banco de dados os ids dos filmes favoritados pelo usuário // api.filmes_populares() / FilmeFavorito.listar() 

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
filme_controller.py 
@classmethod
    def buscar_por_tmdb(cls, tmdb_id):
        return cls.query.filter_by(tmdb_id=tmdb_id).first()


**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
POST, "/adicionar/<int:tmdb_id>"

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

não acontece nada

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

no app.py 
app.register_blueprint(dashboard_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)


**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
favoritos_bp.route("/")
def listar():
    return render_template(
    "favoritos/lista.html",
    favoritos=FilmeFavorito.listar(),
    )


**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Model /  Quem chama: O Controller, para solicitar os dados dos filmes já limpos e formatados

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

 nao sei
---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

Na pasta templates, dentro do diretório de visualização (views).

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

 O template base é o views/templates/layout.html

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

StreamFlix: {{ url_for('dashboard.index') }}
Populares: {{ url_for('filmes.populares') }}
Melhores: {{ url_for('filmes.melhores') }}
Buscar: {{ url_for('filmes.buscar') }}
Favoritos: {{ url_for('favoritos.listar') }}

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

. O arquivo HTML que exibe essa seção é o filmes/detalhe.html (caminho completo: views/templates/filmes/detalhe.html)

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

O arquivo filmes/_card.html é um pedaço reutilizado (também chamado de partial ou componente), Ele é incluído pelas páginas que listam múltiplos filmes, como a página principal

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
A variável booleana que controla o botão é favorito

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

O arquivo CSS do site está localizado em views/static/css/style.css

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
O loop Jinja percorre os registros utilizando a estrutura {% for fav in favoritos %}.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
O {% if modo_demo %} serve para exibir uma barra de aviso no topo do site caso a aplicação esteja rodando sem uma chave de API válida (usando dados de demonstração offline). Quem disponibiliza essa variável globalmente para todos os templates é o @app.context_processor no arquivo principal app.py

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.


View (detalhe.html): O usuário clica em "Salvar favorito", enviando os dados do filme via formulário POST
Controller (favoritos_controller.py): Recebe a requisição e aciona o Model de favoritos
Model (filme_favorito.py): Grava as informações do filme permanentemente no banco de dados SQLite local.Redirect:
O Controller redireciona o usuário de volta para a mesma página de detalhes (filmes.detalhe), atualizando a tela para exibir o botão "Remover"
Arquivos envolvidos:views/templates/filmes/detalhe.html (View)controllers/favoritos_controller.py (Controller)models/filme_favorito.py (Model)
---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
