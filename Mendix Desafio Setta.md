# Objetivos

<input type="checkbox" id="name" name="name"/>


AcessarUsuário do sistema
Eu quero: Saber qual a eficiência da minha máquina de acordo com a temperatura atual e observar a tendência em um gráfico de linha
Para: Tomar a decisão mais lucrativa de acordo com as informações apresentadas no software

Resumo:

O sistema deve disponibilizar para o usuário uma página onde é possível visualizar a temperatura e a eficiência da máquina atuais, além de um gráfico de linha com o histórico dessas duas informações. 

Informações para o cálculo de eficiência da máquina:

É possível observar que a máquina funciona melhor a medida que a temperatura do ambiente está mais quente,
sendo que a partir de 28° a eficiência da máquina é de 100%, e abaixo de 24° a eficiência da máquina registra o pior índice de eficiência, 75%. O comportamento da eficiência entre essas duas temperaturas varia linearmente, de forma diretamente proporcional.

Requisitos da página inicial:

O sistema deve disponibilizar uma página inicial;
A página inicial deve ser atualizada a cada 30 segundos;
Sempre que a página carregar, o sistema deve escrever em um banco de dados externo os valores:
-Data e Hora;
-Temperatura (°C);
-Eficiência da máquina (%);
Sempre que a página carregar, o sistema deve atualizar as informações na tela:
-Data e Hora da última consulta;
-Temperatura da última consulta (°C);
-Eficiência da máquina da última consulta (%);
Sempre que a página carregar, o sitema deve atualizar um gráfico de linha com as informações de temperatura e eficiência da máquina ao longo do tempo;

Requisitos:

A aplicação deve ser desenvolvida utilizando Mendix;
A consulta das informações de temperatura deve utilizar API REST;
O registro das informações no banco externo deve utilizar Queries SQL;
A página precisa apresentar as informações de forma coerente para usuário;

Observações:

Pode ser utilizada qualquer versão do Mendix Studio Pro (Recomendado 9.19);
Pode ser utilizado qualquer serviço para consulta de temperatura (Recomendado OpenWeather);
Pode ser utilizado qualquer banco de dados SQL para registro das informações (Recomendado PostgreSQL 12);
O banco de dados SQL pode estar hospedado no localhost;
Não é necessário fazer deploy da aplicação;
Incrementos na lógica serão avaliados como diferenciais na entrega;
O design da página será avaliado como diferencial na entrega;

Documentação de apoio:

https://marketplace.mendix.com/link/studiopro/9.19.0
https://marketplace.mendix.com/link/component/2888
https://openweathermap.org/current

Ao final, pense em melhorias funcionais para o sistema que contribuam para gerar valor ao usuário.


# Dicionario
Nanoflow é igual a um microflow só que acontece no lado do cliente


# Interface grafica

Videos do Leo Andrade

Videos dos Academia Mx Brasil

# Evento Progamado

https://docs.mendix.com/refguide/scheduled-events/#1-introduction


# Calculo da Eficienca

# Buscando API

https://www.youtube.com/watch?v=wJJmxx64J6c

# PostgreSQL

https://www.youtube.com/watch?v=UbX-2Xud1JA

https://youtu.be/4uYI-kg-dZw

user:postgres
password: 1234
