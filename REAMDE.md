### ELK Stack != Elastic Stack
ELK stack -> L vem de Logstash que é muito difícil de se trabalhar. Por isso, está caindo em desudo
Elastic Stack -> Usa o mais moderno Beats (FileBeat, MetricBeat, Audit).

### Para estudar
A parte de audit do Beats -> Pode resolver problema de segurança de rastreamento de operações no sistema?

### Métricas
- De onde pegar -> do servidor, do docker, do k8s? O metric beats consegue pegar métricas de todos esses lugares. Vale a pena averiguar o que faz mais sentido para o caso específico
- Para usar o Metricbeat é necessário instalá-lo no servidor que se deseja monitorar e configurar (a partir de um arquivo). Essa config diz quais configs do elastic search vão mandar as informações de métricas
- Para configurar métricas de docker não é necessário instalar o metricbeat? - **Dúvida**

### Uptime e heartbeat
- requisições http nas urls e pings nos servidores definido(a)s para ver se está tudo em cima
- No kibana são mostrados gŕaficos **Muito bacanas e insightfulls** sobre quais serviços estão em pé e quais não estão

### Elastic APM
- Trabalha com rastreabilidade


## Na cloud
- Dá para configurar o agente do apm direto na cloud (mesmo que rodando localmente) pelas chaves que o elasticsearch provê
- É possível ativar os dashboards padrões das aplicações mais comuns (rabbitmq, nginx, etc) no kibana

## Observações:
    Comandos do python como pdm, poetry e qq outra lib pode ser rodada quando é instalada para o usuário root. Para outros usuários, é necessário por no path ou chamar a partir de python -m "nome-da-lib"
