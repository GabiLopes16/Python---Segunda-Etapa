[
  {
    "ano": 1949,
    "autor": "George Orwell",
    "data_criacao": "2026-07-31 10:20:01.608065",
    "id": 6,
    "titulo": "1984"
  },
  {
    "ano": 2026,
    "autor": "3A1",
    "data_criacao": "2026-07-31 10:35:38.648356",
    "id": 10,
    "titulo": "Cotemig"
  },
  {
    "ano": 1899,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-31 10:19:55.836824",
    "id": 5,
    "titulo": "Dom Casmurro"
  },
  {
    "ano": 1899,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-31 10:35:33.093321",
    "id": 9,
    "titulo": "Dom Casmurro"
  },
  {
    "ano": 1966,
    "autor": "Daniel Keyes",
    "data_criacao": "2026-07-31 10:36:18.171632",
    "id": 17,
    "titulo": "Flores para Algernon"
  },
  {
    "ano": 1997,
    "autor": "J.K. Rowling",
    "data_criacao": "2026-07-31 10:35:59.158329",
    "id": 13,
    "titulo": "Harry Potter"
  },
  {
    "ano": 1988,
    "autor": "Paulo Coelho",
    "data_criacao": "2026-07-31 10:19:21.602657",
    "id": 4,
    "titulo": "O Alquimista"
  },
  {
    "ano": 1988,
    "autor": "Paulo Coelho",
    "data_criacao": "2026-07-31 10:35:27.813284",
    "id": 8,
    "titulo": "O Alquimista"
  },
  {
    "ano": 1925,
    "autor": "F. Scott Fitzgerald",
    "data_criacao": "2026-07-31 10:36:14.468537",
    "id": 16,
    "titulo": "O Grande Gatsby"
  },
  {
    "ano": 1943,
    "autor": "Antoine de Saint-Exup\u00e9ry",
    "data_criacao": "2026-07-31 10:20:39.036302",
    "id": 7,
    "titulo": "O Pequeno Pr\u00edncipe"
  }
]


PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"O Alquimista","autor":"Paulo Coelho","ano":"1988"}'
>>

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Dom Casmurro","autor":"Machado de Assis","ano":"1899"}'
>>

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"O Pequeno Principe","autor":"Antoine de Saint-Exupery","ano":"1943"}'
>>

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"O Pequeno Principe","autor":"Antoine de Saint-Exupery","ano":"1943"}'
>>

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"O Hobbit","autor":"J.R.R. Tolkien","ano":"1937"}'
>>

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Harry Potter","autor":"J.K. Rowling","ano":"1997"}'

>>
Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"Torto Arado","autor":"Itamar Vieira Junior","ano":"2019"}'


  Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"A Hora da Estrela","autor":"Clarice Lispector","ano":"1977"}'


Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"O Grande Gatsby","autor":"F. Scott Fitzgerald","ano":"1925"}'


Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"Flores para Algernon","autor":"Daniel Keyes","ano":"1966"}'


PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros/10 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros/12 -Method DELETE

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros/14 -Method DELETE

PS C:\Users\12501174> Invoke-RestMethod http://127.0.0.1:5000/api/livros/15 -Method DELETE