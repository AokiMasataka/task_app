# FROM node:18 as build-stage

# WORKDIR /app
# COPY package*.json ./
# COPY ./ .
# RUN npm install

# RUN npm run build
# COPY  --from=build-stage /app/dist /usr/share/nginx/html

FROM nginx:stable-perl as production-stage

COPY ./dist /usr/share/nginx/html
