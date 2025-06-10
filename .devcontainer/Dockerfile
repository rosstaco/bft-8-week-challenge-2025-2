FROM node:20-bullseye

# Install additional tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install global npm packages
RUN npm install -g @docusaurus/init serve

# Set working directory
WORKDIR /workspace

# Create non-root user
RUN groupadd --gid 1000 node \
    && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# Switch to non-root user
USER node

# Set default command
CMD ["bash"]
