FROM armhf/alpine:3.5
RUN apk add --update nginx
RUN mkdir -p /run/nginx/
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/html/
RUN echo "<html>Welcome to Kaspers Raspberry Pi!</html>" | tee -a /var/www/html/index.html

COPY raspberrypi.conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
