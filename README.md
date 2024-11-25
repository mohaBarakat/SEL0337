# SEL0337

## Parte 1

Para a parte 1, foi escolhido um programa de inicialização (ExecStart) que pisca um LED vermelho (arquivo blink_led.py) e quando o arquivo .service é parado (ExecStop), o LED permanece aceso sem piscar. 
![Alt text](img/terminal.jpg)
Para isso foi feito um circuito, no qual o GPIO 2 da Raspberry pi é conectado ao catodo de um LED, enquanto o anodo permanece aterrado.