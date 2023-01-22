# Bot-Avaliacao-Docente-UFMG

Script para responder automaticamente o questionário de avaliação docente da UFMG. Útil
para matérias com muitos professores cadastrados no sistema. Já me salvou várias horas
ao longo da graduação e espero que possa ajudar outras pessoas também. 

---

## Última atualização

2023/1

## Como executar

Fazer o download do executável no [link](https://github.com/joao-gabrielC/Bot-Avaliacao-Docente-UFMG/releases/download/v0.1.0/Bot-Avaliacao-Docente-UFMG.exe).
Depois, basta executar o arquivo e seguir as instruções que aparecem na tela. Se quiser avaliar algum
professor, responda manualmente antes de executar o script já que em todos os
professores não avaliados será marcada a opção de "não desejo responder".


## Limitações

- Se houver mais de uma página, o script só acessa os nomes da primeira página.
Para contornar isso, passe a página manualmente e o script conseguirá reconhecer
os próximos nomes automaticamente.

## Requerimentos

- selenium
- webdriver\_manager
