After clone this repositoy navitage to its folder and run

`python poc.py`

This file will install the maven archetype on your local maven repository then will ask some questions to create a new projetc.

Example:

```text
PS C:\poc-archetype> python poc.py

Qual nome da Aplicação? (Sem Espaço) TestePy
Digite o Groupid: br.com.tamawilson
Digite o ArtifactId: teste-py
Incluir Lombok? (S/N) s
Incluir Postgres? (S/N) s
```
After those questions you will find the created project on a upper folder outside this repository folder.