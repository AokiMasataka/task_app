FROM denoland/deno:latest AS build-stage

WORKDIR /app
COPY ./ .
RUN deno task build

FROM nginx:stable-perl AS production-stage

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /app/dist /usr/share/nginx/html
