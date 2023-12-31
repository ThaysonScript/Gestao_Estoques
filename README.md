## 1. Desenvolvimento de um software para controle e gerenciamento de estoques.

Apresentamos o Desenvolvimento de um Software Especializado em Cadastro de Fabricante, Modelo e serial/código do item.
Este sistema simplificado e focado oferece uma solução eficaz para empresas que buscam gerenciar de forma eficiente 
as informações essenciais de seus produtos, a fim de agilizar processos e garantir a precisão dos registros.

## 2. Recursos Destacados:
### 2.1 **Menu de Usuario Principal:**
#### Uma interface de linha de comando/terminal simplificada e direto ao ponto para que o usuário vá direto a sua escolha de interesse, como, cadastros, leituras, edições e remoções.

### 2.2 **Cadastro Simplificado:** 
#### O software oferece uma interface intuitiva e descomplicada para o cadastro de ( fabricantes, modelos e serial/código do item ), ou seja, pelo menos 3 propriedades.
#### Com poucos cliques, os usuários podem inserir informações cruciais sobre seus produtos.

### 2.3 **Consulta Rápida de Items em Estoque ( e suas propriedades ):**
#### 2.3.1. buscar por nome do item:
##### Aqui o usuário pode digitar o nome do seu fabricante e verificar se ele esta cadastrado no estoque.

### 2.3.2. buscar por propriedade do item:
#### Aqui o usuário pode digitar tanto o seu fabricante e retornar as propriedades dele, como, o proprio fabricante, modelo e codigo do item, como, a partir do fabricante, modelo ou codigo, encontrar:
```
FABRICANTE -> modelo ou codigo;
MODELO -> fabricante ou codigo;
CODIGO -> fabricante ou modelo.
```

### 2.4 **Edição de Items por seu Nome (fabricante) ou por suas Propriedades Cadastradas:**
#### O sistema permite atualizações e edições sem complicações.
#### O Usuario pode fazer edições e atualizar seus items que acabaram de ser cadastrados no sistema caso aquele registro tenha mudado ou erro ao cadastrar o item.
#### A Principal Maneira de editar/atualizar seu item é:
```
- por nome (fabricante), identificar o item cadastrado a ser futuramente editado, senão, digite somente enter:
- fabricante, retornar a atual fabricante e poder alterar por uma nova se desejar, senão, digite somente enter;
- modelo, retornar o modelo atual cadastrado e permitir a edição desse modelo, senão, digite somente enter;
- codigo de produto, retornar o codigo do produto atual e permite a edição desse codigo, senão, digite somente enter.
```

### 2.6 **Persistência de dados em Arquivos .csv:** 
#### Todas as informações cadastradas, atualizadas ou deletadas são armazenadas e atualizadas em um arquivo.csv, permitindo um acesso rápido e de fácil para consulta.
#### Isso elimina a necessidade de rastrear informações dispersas e complexas em diferentes sistemas ou documentos físicos.
