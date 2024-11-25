# SEL0337

## Parte 1

Para a parte 1, foi escolhido um programa de inicialização (ExecStart) que pisca um LED vermelho (arquivo blink_led.py) e quando o arquivo .service é parado (ExecStop), o LED permanece aceso sem piscar. Para isso foi feito um circuito, no qual o GPIO 2 da Raspberry pi é conectado ao catodo de um LED, enquanto o anodo permanece aterrado. Além disso, o arquivo .service utilizado foi o ![blink.service](blink.service). Os comandos no terminal podem ser visto na foto a seguir.

![Foto Terminal](img/terminal.jpg)

Além do que foi mostrado na foto, foi utilizado o comando sudo systemctl daemon-reload.

O código utilizado após o reboot da Raspberry pi foi o código ![blink_led.py](blink_led.py) e pode ser visto em ![Vídeo de funcionamento incial](img/parte1_start.mp4). Já o código de parada é o ![blink_stop.py](blink_stop.py) e pode ser visto na foto a seguir.

![Foto Terminal](img/parte1_stop.jpg)