# Prototype 01: 
Nesse prototipo eu testei como funciona o banco de dados da supabase e como usa-lo da forma mais simples possivel, nesse prototipo, por ser o primeiro eu não me preocupei como nada a não ser se vai se comunicar com a DB, e funcionou, ainda é bem ruim, bugs conseguem ser perceptiveis rapidamente e não demora muito para ficar sobrecarregado, precisa de melhoras em basicamente tudo, mas pelo menos ele cumpre oque eu quis fazer nele(testar a comunicação com a DB).

Futuras mudanças:
- interface grafica
- melhor a conecção com o banco de dados(mais rapida e eficiente)
- melhorar a forma com que pega a hora atual
- melhorar como as mensagens são exibidas 
- mostrar as mensagens em tempo real

# Prototype 02: 
Nesse prototipo eu queria implementar uma representação visual no sistema, grande parte do codigo é cheio de gambiarras mas foi um ponta-pé inicial para a criação de uma interface para o sistema.

Futuras mudanças:
- procurar alguma forma de mostrar uma mensagem de "nome invalido" sem ser com o messagebox
- fazer de uma forma mais eficiente os placeholders ja que copiar e colar codigo é vergonhoso
- achar uma forma de substituir os metodos de posicionamento de widgets(grid, pack e o place) ja que eles não atendem as espectativas de uso
- melhorar o visual 
- entender melhor conceitos do tkinter para evitar conflitos e melhorar a experiencia
- melhor conecção com o banco de dados(mais rapida e eficiente) ⚠
- separar as funções do codigo principal, ja que deixa o codigo bem mais complexo
- mostrar a hora de envio de mensagens novamente
- melhorar o sistema de envio de mensagem
- melhorar como as mensagens são mostradas
- o usuario que digitou a mensagem ficará a direita
- não aceitar espaços 

obs: melhorar o sistema de atualização(me arrependo de minhas escolhas)

# Prototype 03:
Nesse prototipo eu decidi testar e melhorar algumas coisas como os metodos de geometria ou a aparencia da interface por exemplo.
Tambem decidi deixar o chat em tempo real.

Futuras mudanças:
- salvar o nome(e não criar uma variavel temporaria)
- achar uma forma de substituir os metodos de posicionamento de widgets(grid, pack e o place) ja que eles não atendem as espectativas de uso 
- separar as funções do codigo principal, ja que deixa o codigo bem mais complexo ⚠
- buscar um jeito mais simples de estabalecer a conecção com o server(talvez criando um arquivo que faça isso e o programa principal só tenha que ler o arquivo)
- criar classes para melhorar os widgets
- optimizar a exibição de mensagens(não carregar todas de uma só vez)
- voltar(e melhorar) os placeholders
- mostrar a hora que a mensagem foi enviada ⚠
- o usuario que digitou a mensagem ficará a direita
- adicionar um filtro no envio de mensagens(evitar spam)
- quebrar a linha quando ultrapassar o limite da caixa
- adicionar os placeholder novamente nas caixas de entrada

# Prototype 04:
Nesse prototipo eu decidi testar como vai funcionar ter multiplas paginas para melhorar a experiencia do usuario e multiplos arquivos para facilitar a compreenção do codigo.

Futuras mudanças:
- melhorar a estrutura do codigo
- começar a utilização do ttk
- adicionar uma ORM melhor
- adicionar todas as funcionalidades do prototype03 

# Prototype 04.1
Por problema no desenvolvimento do Prototype 04 eu vi necessidade de criar uma nova versão do mesmo refazendo ele para conseguir entregar oque foi proposto no prototype 04.