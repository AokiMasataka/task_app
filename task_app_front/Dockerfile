FROM denoland/deno:latest AS build-stage

WORKDIR /app
COPY ./ .
RUN deno task build

FROM nginx:stable-perl AS production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
