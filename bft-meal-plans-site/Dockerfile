# Multi-stage build for BFT Meal Plans Docusaurus site

# Stage 1: Build the Docusaurus site
FROM --platform=$BUILDPLATFORM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build the site
RUN npm run build

# Stage 2: Serve with Nginx
FROM --platform=$TARGETPLATFORM nginx:alpine

# Copy the built site from the builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Create a simple nginx config that listens on port 8080
RUN echo 'server {\
    listen 8080;\
    listen [::]:8080;\
    server_name _;\
    \
    root /usr/share/nginx/html;\
    index index.html index.htm;\
    \
    location / {\
    try_files $uri $uri/ /index.html;\
    }\
    \
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {\
    expires 1y;\
    add_header Cache-Control "public, immutable";\
    }\
    \
    # Security headers\
    add_header X-Frame-Options "SAMEORIGIN" always;\
    add_header X-XSS-Protection "1; mode=block" always;\
    add_header X-Content-Type-Options "nosniff" always;\
    add_header Referrer-Policy "no-referrer-when-downgrade" always;\
    add_header Content-Security-Policy "default-src '\''self'\'' http: https: data: blob: '\''unsafe-inline'\''" always;\
    }' > /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
