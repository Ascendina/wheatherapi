# Wheather API ✨ 
A distributed system to obtain weather data from the free weather API using Python (Flask, Celery, and Redis).
😎

## Project - How it works  🙋‍♂️
This project utilizes the following Python frameworks: Flask, Celery, and Redis. The diagram below explains how these software components communicate with each other and what roles they play within the system.

<div align="center">
  <img src="https://github.com/Ascendina/wheatherapi/blob/main/diagrama_flask_celery_redis.png" alt="ProjectDiagram" style="width:50%;"/>
</div>

The client (user) makes a request, and Flask, a web framework, handles the HTTP requests, routing, and responses to the user. After that, Redis functions as a memory storage and message broker for Celery. Finally, Celery manages asynchronous task processing (fetching weather values from the free weather API and returning the processing percentage).

Beyond these frameworks, unittest and coverage (Python) were used to implement automated testing.

## How to Run 

Cansado de READMEs chatos e monótonos? Dê uma olhada nos nossos [templates de repositório](https://github.com/DiasEllen26/template-readme/tree/main/repositorio) e deixe seus projetos brilharem! Nossos modelos oferecem uma estrutura flexível e divertida para documentar seu projeto, incluindo seções para descrição, instalação, uso, contribuição e licença.

## Status 🚀

Deixe o mundo saber como está o seu projeto! Adicione cards de status e informe o estado do build, cobertura de testes, análise de código e muito mais. Os cards de status são uma maneira divertida e visual de fornecer informações importantes sobre o seu projeto.

## Linguagens 🚀

Mostre suas habilidades de programação com estilo! Utilize nossos ícones de linguagens para destacar as tecnologias envolvidas em seus projetos. Esses ícones são amplamente reconhecidos pela comunidade de desenvolvedores e adicionam um toque especial ao seu README.

---

## Contribuição 🤝📚😄

Este é um projeto de código aberto e adoraríamos receber contribuições da comunidade de desenvolvedores! Sinta-se à vontade para fazer fork deste repositório, trabalhar em melhorias e enviar pull requests para análise.

Se você encontrar problemas ou tiver sugestões, abra uma issue e teremos prazer em discuti-las.

Lembre-se de seguir as diretrizes de contribuição do projeto e respeitar o código de conduta.

Junte-se a nós para tornar este projeto ainda mais incrível!

