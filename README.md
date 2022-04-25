# Documentação

Esta API não requer autenticação para acessá-la.

REST
Base url: https://leads-rest-api.herokuapp.com

---

# Registrar uma lead

Rota registra um novo Lead no banco de dados.

`Post /leads - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000"
}
```

`Post /leads - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000",
  "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
  "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
  "visits": 1
}
```

---

# Buscar todas as leads

Lista todos os LEADS por ordem de visitas, do maior para o menor.

`Get /leads - FORMATO DA REQUISIÇÃO`

`Não há.`

`Get /leads - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
  },
  {
    "name": "John Doe1",
    "email": "john1@email.com",
    "phone": "(41)80000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
  }
]
```

---

# Atualiza uma lead

Atualiza apenas o valor de visits e last_visit em cada requisição.

`Patch /leads - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

`Patch /leads - FORMATO DA RESPOSTA - STATUS 204`

`Não há.`

---

# Exclui uma lead

Deleta um Lead específico.

`Delete /leads - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

`Delete /leads - FORMATO DA RESPOSTA - STATUS 204`

`Não há.`
