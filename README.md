# Simulated-annealing-8-queens

### Trabalho de Inteligência Artificial que consiste em um código que resolve o problema das 8 rainhas junto com uma têmpera simulada.<br>
>Colaboradoras: Eduarda Elger ([GitHub Profile](https://github.com/EduardaElger)), Ellen Bonafin ([GitHub Profile](https://github.com/EllenBonafin)) e Heloisa Alves ([GitHub Profile](https://github.com/Helogizzy))

<br>**Problema:**<br>

 Em um tabuleiro NxN temos N rainhas, o objetivo é colocar as rainhas no tabuleiro de forma em que elas não se ataquem. No xadrez as rainhas podem se movimentar na vertical, horizontal e diagonal. Para facilitar a implementação foi considerado:
 - Nunca terá mais de uma rainha na mesma coluna.
 - A contagem de ataques sempre será da rainha atual para frente, nunca será feita a contagem para trás.
 
 Ao longo da execução temos uma temperatura setada em 1.000.000 que vai diminuindo após cada interação.<br>
 
 <br>**Condições de parada:**<br>
 - Caso o problema seja resolvido antes da temperatura esfriar o código para e mostra a melhor solução encontrada.
 - Caso a temperatura chegue perto de 1 o código para o seu processamento, a solução não foi encontrada. 

<br>**Sobre o código:**<br>
- O número de ataques, temperatura e o tabuleiro são apresentados via terminal.<br>
- O código funciona para quaisquer dimensões, basta mudar o número de N na linha 8:
```
global N 
N = 8
```
<br>
 <br>
