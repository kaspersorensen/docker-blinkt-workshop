FROM armhf/alpine:latest
RUN apk add --update nginx && \
    mkdir -p /run/nginx/ && \
    rm /etc/nginx/conf.d/default.conf && \
    mkdir -p /var/www/html/ && \
		echo "<html>Welcome to Kaspers Raspberry Pi!</html>" | tee -a /var/www/html/index.html

COPY raspberrypi.conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]