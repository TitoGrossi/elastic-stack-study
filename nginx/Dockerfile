FROM nginx:latest

# Pegar os erros reais, não o link simbólico dos logs no stdout
RUN rm -f /var/log/nginx/access.log && rm -f /var/log/nginx/error.log

COPY default.conf /etc/nginx/conf.d/default.conf

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

COPY filebeat.yml /etc/filebeat/filebeat.yml

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
