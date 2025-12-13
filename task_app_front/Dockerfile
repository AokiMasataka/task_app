FROM denoland/deno:latest AS build-stage

# ARG VITE_BACKEND_HOST
# ENV VITE_BACKEND_HOST=${VITE_BACKEND_HOST}
# ARG VITE_BACKEND_PORT
# ENV VITE_BACKEND_PORT=${VITE_BACKEND_PORT}

ARG VITE_BACKEND_API_BASE_URL
ENV VITE_BACKEND_API_BASE_URL=${VITE_BACKEND_API_BASE_URL}

WORKDIR /app
COPY ./ .
RUN deno task build

FROM nginx:stable-perl AS production-stage

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /app/dist /usr/share/nginx/html
