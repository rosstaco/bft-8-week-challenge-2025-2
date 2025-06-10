q# BFT Challenge - Docusaurus Setup Instructions

## 📋 Current Status

✅ **Completed:**
- All 8 weekly meal plans created in markdown format
- Dev container configuration set up with Node.js 20
- Docker-in-Docker capability configured
- README.md with navigation links created

🚀 **Next Steps:**
- Set up Docusaurus site
- Configure meal plans in Docusaurus
- Create Docker container for deployment

## 🛠️ Setup Instructions

### Step 1: Open in Dev Container

1. **Reopen in Container:**
   - Press `Cmd+Shift+P` (macOS)
   - Type "Dev Containers: Reopen in Container"
   - Wait for container to build (first time may take a few minutes)

2. **Verify Environment:**
   ```bash
   node --version    # Should show v20.x
   npm --version     # Should show npm version
   docker --version  # Should show Docker version
   ```

### Step 2: Create Docusaurus Site

1. **Create the documentation site:**
   ```bash
   # Create a new directory for the site
   mkdir bft-meal-plans-site
   cd bft-meal-plans-site
   
   # Initialize Docusaurus
   npx create-docusaurus@latest . classic --typescript
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Test the initial setup:**
   ```bash
   npm start
   ```
   - Should open on `http://localhost:3000`
   - Port 3000 is already forwarded in the dev container

### Step 3: Configure Meal Plans

1. **Copy meal plan files:**
   ```bash
   # Create docs directory structure
   mkdir -p docs/meal-plans
   
   # Copy all meal plan markdown files
   cp ../Week_*_Meal_Plan.md docs/meal-plans/
   ```

2. **Update docusaurus.config.ts:**
   ```typescript
   // Update the config file with:
   title: 'BFT 8 Week Challenge',
   tagline: 'Your Complete Meal Planning Guide',
   url: 'https://your-domain.com',
   baseUrl: '/',
   
   // Update navbar
   navbar: {
     title: 'BFT Challenge',
     items: [
       {
         type: 'doc',
         docId: 'intro',
         position: 'left',
         label: 'Meal Plans',
       },
     ],
   },
   ```

3. **Create sidebar configuration:**
   ```bash
   # Edit sidebars.ts to organize meal plans
   ```

### Step 4: Customize Content

1. **Update docs/intro.md:**
   ```markdown
   # BFT 8 Week Challenge
   
   Welcome to your complete meal planning guide!
   
   ## Weekly Meal Plans
   
   - [Week 1](meal-plans/Week_1_Meal_Plan)
   - [Week 2](meal-plans/Week_2_Meal_Plan)
   - ... (continue for all weeks)
   ```

2. **Add meal plan metadata:**
   Add frontmatter to each meal plan file:
   ```markdown
   ---
   sidebar_position: 1
   title: Week 1 Meal Plan
   ---
   ```

### Step 5: Build and Test

1. **Build the site:**
   ```bash
   npm run build
   ```

2. **Serve the built site:**
   ```bash
   npm run serve
   ```

### Step 6: Create Docker Container

1. **Create Dockerfile:**
   ```dockerfile
   # Create in bft-meal-plans-site directory
   FROM nginx:alpine
   
   # Copy the built site
   COPY build/ /usr/share/nginx/html/
   
   # Copy custom nginx config if needed
   # COPY nginx.conf /etc/nginx/nginx.conf
   
   EXPOSE 80
   
   CMD ["nginx", "-g", "daemon off;"]
   ```

2. **Create docker-compose.yml:**
   ```yaml
   version: '3.8'
   services:
     bft-meal-plans:
       build: .
       ports:
         - "8080:80"
       restart: unless-stopped
   ```

3. **Build and test Docker image:**
   ```bash
   # Build the Docusaurus site first
   npm run build
   
   # Build Docker image
   docker build -t bft-meal-plans .
   
   # Run container
   docker run -p 8080:80 bft-meal-plans
   ```

## 📁 Expected File Structure After Setup

```
bft-meal-plans-site/
├── docs/
│   ├── intro.md
│   └── meal-plans/
│       ├── Week_1_Meal_Plan.md
│       ├── Week_2_Meal_Plan.md
│       └── ... (all weeks)
├── src/
├── static/
├── docusaurus.config.ts
├── sidebars.ts
├── package.json
├── Dockerfile
└── docker-compose.yml
```

## 🎯 Customization Options

### Theme Customization
```bash
# Add custom CSS
mkdir src/css
# Edit src/css/custom.css for styling
```

### Add Search
```bash
# Install Algolia DocSearch or local search
npm install @docusaurus/theme-search-algolia
```

### Add Analytics
```bash
# Add Google Analytics
npm install @docusaurus/plugin-google-analytics
```

## 🚀 Deployment Options

### Option 1: Netlify
1. Build: `npm run build`
2. Deploy: Upload `build/` folder

### Option 2: Vercel
1. Connect GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `build`

### Option 3: Docker (Self-hosted)
1. Build image: `docker build -t bft-meal-plans .`
2. Run: `docker run -p 80:80 bft-meal-plans`

### Option 4: Docker Compose
```bash
docker-compose up -d
```

## 🔧 Troubleshooting

### Common Issues:
1. **Port conflicts:** Change ports in docker-compose.yml
2. **Build errors:** Check Node.js version compatibility
3. **Markdown issues:** Ensure proper frontmatter format

### Useful Commands:
```bash
# Clear cache
npm run clear

# Typecheck
npm run typecheck

# Start in development mode
npm run start

# Build for production
npm run build
```

## 📝 Notes

- All meal plan markdown files are already formatted correctly
- The dev container has all necessary tools installed
- Port 3000 (dev) and 8080 (production) are forwarded
- Docker-in-Docker is available for building containers

## 🎉 Final Steps

Once everything is working:
1. Test all meal plan pages
2. Verify responsive design
3. Build and test Docker container
4. Choose deployment method
5. Deploy to production

---

**Ready to start?** Begin with Step 1 and open this workspace in the dev container!
