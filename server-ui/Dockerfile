# ------------------------------------------------------------
# Stage 1 - Build Angular application
# ------------------------------------------------------------
FROM node:24-alpine AS builder

WORKDIR /app

# Copy dependency files first (better layer caching)
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy application source
COPY . .

# Build production bundle
RUN npm run build

# ------------------------------------------------------------
# Stage 2 - Runtime
# ------------------------------------------------------------
FROM nginx:1.28-alpine

# Remove default website
RUN rm -rf /usr/share/nginx/html/*

# Copy Angular build output
COPY --from=builder /app/dist/server-ui/browser/ /usr/share/nginx/html/

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
