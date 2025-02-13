FROM denoland/deno:latest as build-stage

WORKDIR /app
COPY ./ .
run deno task build

FROM nginx:stable-perl as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
