FROM node:lts-alpine
#FROM node:12
RUN mkdir /app
COPY . /app
#ADD . /app
WORKDIR /app
#COPY package*.json ./


#/app/node_modules/http-server/bin
RUN npm install
ENV PATH=$PATH:/app/node_modules/http-server/bin
#COPY . .

EXPOSE 8080

#RUN ls -la /app/node_modules/.bin

ENTRYPOINT ["node", "/app/node_modules/http-server/bin/http-server", "-s"]
