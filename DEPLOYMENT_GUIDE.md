# 🚀 STEP-BY-STEP DEPLOYMENT GUIDE
## Market Basket Analysis Dashboard - Streamlit Cloud

**Total Time Estimate**: 30-45 minutes
**Cost**: $0 (FREE)
**Difficulty**: Beginner-friendly

---

## ✅ Pre-Deployment Checklist

Before you begin, ensure you have:
- [ ] Windows PC with internet connection
- [ ] All files in `mba_dashboard_deploy` folder
- [ ] Python 3.8+ installed
- [ ] Email address for account creation

---

## 📦 PHASE 1: Local Testing (15-20 minutes)

### Step 1.1: Install Python (if not already installed)

1. Check if Python is installed:
   ```bash
   python --version
   ```

2. If not installed, download from [python.org](https://www.python.org/downloads/)
   - Choose version 3.8 or higher
   - During installation, CHECK "Add Python to PATH"

### Step 1.2: Install Required Packages

Open Command Prompt or PowerShell in the `mba_dashboard_deploy` folder:

```bash
# Navigate to the folder
cd C:\Users\emman\p_Claude\big_data\w1\mba_dashboard_deploy

# Install dependencies
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed streamlit-1.29.0 pandas-2.1.0 plotly-5.17.0 networkx-3.2
```

### Step 1.3: Run App Locally

```bash
streamlit run app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Step 1.4: Test the App

1. Browser should open automatically to `http://localhost:8501`
2. If not, manually open the URL
3. **Test these features**:
   - [ ] Dashboard loads with statistics
   - [ ] Left sidebar shows filters
   - [ ] Adjust support slider → rules table updates
   - [ ] Adjust confidence slider → rules table updates
   - [ ] Adjust lift slider → rules table updates
   - [ ] Search for "Coffee" → filtered results appear
   - [ ] Click on "Visualizations" tab → charts display
   - [ ] Click on "Network Graph" tab → graph displays
   - [ ] Download CSV button works
   - [ ] No error messages in browser

4. **Stop the app**: Press `Ctrl+C` in Command Prompt

✅ **If everything works locally, proceed to deployment!**

---

## 🌐 PHASE 2: GitHub Setup (10-15 minutes)

### Step 2.1: Create GitHub Account (if needed)

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Enter email, create password, choose username
4. Verify email address
5. Choose "Free" plan

### Step 2.2: Install Git (if not already installed)

1. Check if Git is installed:
   ```bash
   git --version
   ```

2. If not installed, download from [git-scm.com](https://git-scm.com/download/win)
   - Use default settings during installation
   - Restart Command Prompt after installation

### Step 2.3: Configure Git (first-time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 2.4: Create GitHub Repository

**Option A: Via GitHub Website** (Recommended for beginners)

1. Go to [github.com](https://github.com)
2. Click green "New" button (or "+" icon → "New repository")
3. Repository name: `mba-dashboard`
4. Description: `Market Basket Analysis Interactive Dashboard`
5. Select: **Public**
6. **DO NOT** check "Add a README file"
7. Click "Create repository"
8. **Keep this page open** - you'll need the commands shown

**Option B: Via Command Line** (if you have GitHub CLI)

```bash
gh repo create mba-dashboard --public --description "Market Basket Analysis Dashboard"
```

### Step 2.5: Push Code to GitHub

In Command Prompt, navigate to your folder:

```bash
cd C:\Users\emman\p_Claude\big_data\w1\mba_dashboard_deploy

# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - MBA Dashboard for assignment"

# Rename branch to main
git branch -M main

# Add GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/mba-dashboard.git

# Push to GitHub
git push -u origin main
```

**If prompted for credentials:**
- Username: Your GitHub username
- Password: Use a Personal Access Token (see Step 2.6)

### Step 2.6: Create Personal Access Token (if needed)

1. GitHub.com → Profile picture → Settings
2. Scroll down → Developer settings
3. Personal access tokens → Tokens (classic)
4. Generate new token (classic)
5. Note: "MBA Dashboard deployment"
6. Expiration: 90 days
7. Check: `repo` (all repo permissions)
8. Generate token
9. **Copy the token** (you won't see it again!)
10. Use this token as password when pushing

### Step 2.7: Verify Upload

1. Refresh your GitHub repository page
2. You should see:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `data/` folder with 4 CSV files

✅ **Code is now on GitHub!**

---

## ☁️ PHASE 3: Streamlit Cloud Deployment (5-10 minutes)

### Step 3.1: Create Streamlit Cloud Account

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in"
3. Choose "Continue with GitHub"
4. Authorize Streamlit Cloud to access your GitHub

### Step 3.2: Deploy App

1. Click "New app" button (top right)
2. Fill in the form:
   - **Repository**: Select `YOUR_USERNAME/mba-dashboard`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): `mba-dashboard` or customize
3. Click "Advanced settings" (optional):
   - Python version: 3.9 or 3.10 (default is fine)
4. Click "Deploy!"

### Step 3.3: Wait for Deployment

You'll see a deployment log. This takes 2-5 minutes:

```
[00:00] Creating virtual environment
[00:30] Installing packages from requirements.txt
[01:30] Running app.py
[02:00] App is live!
```

✅ **Your app is now live!**

### Step 3.4: Get Your App URL

URL format: `https://YOUR_USERNAME-mba-dashboard.streamlit.app`

Example: `https://john-mba-dashboard.streamlit.app`

---

## 🎯 PHASE 4: Testing & Verification (5 minutes)

### Step 4.1: Test Deployed App

Open your app URL and verify:
- [ ] Dashboard loads correctly
- [ ] All filters work
- [ ] All visualizations display
- [ ] Network graph renders
- [ ] Download button functions
- [ ] No error messages

### Step 4.2: Mobile Testing (Optional)

- Open URL on your phone
- Check if interface is responsive
- Test basic filtering

### Step 4.3: Share Your URL

**Add to your assignment submission:**
```markdown
## Live Dashboard
**URL**: https://YOUR_USERNAME-mba-dashboard.streamlit.app

The interactive dashboard allows exploration of 42 association rules
from The Bread Basket dataset with dynamic filtering and visualizations.
```

---

## 📸 PHASE 5: Documentation for Assignment (10 minutes)

### Step 5.1: Take Screenshots

Capture these views for your assignment:

1. **Dashboard home** with all metrics visible
2. **Association Rules table** showing top rules
3. **Visualizations tab** with 4-panel chart
4. **Network graph** showing item relationships
5. **Filtered results** (e.g., search for "Coffee")

### Step 5.2: Update Jupyter Notebook

Add a new markdown cell at the end of `MBA_BreadBasket_Business.ipynb`:

```markdown
## Interactive Dashboard Deployment

I have deployed an interactive web application to explore these association rules.

**Live URL**: https://YOUR_USERNAME-mba-dashboard.streamlit.app

### Features:
- Dynamic filtering by support, confidence, and lift thresholds
- Interactive network visualization of item relationships
- 4-panel metric analysis dashboard
- Searchable association rules table
- Download filtered results as CSV

### Technology Stack:
- **Framework**: Streamlit (Python web framework)
- **Visualizations**: Plotly (interactive charts)
- **Hosting**: Streamlit Community Cloud (FREE)
- **Source Code**: https://github.com/YOUR_USERNAME/mba-dashboard

The dashboard enables non-technical stakeholders to explore the market basket
analysis insights without requiring Python knowledge or data analysis skills.
```

### Step 5.3: Create Assignment Appendix

Add to your assignment document:

**Appendix B: Interactive Application**

1. **Purpose**: Enable stakeholders to explore association rules interactively
2. **URL**: [Your Streamlit URL]
3. **Source Code**: [Your GitHub URL]
4. **Features**:
   - Real-time filtering by metrics
   - Interactive visualizations
   - Network graph analysis
   - Export functionality
5. **Deployment**: Streamlit Cloud (free hosting)
6. **Screenshots**: [Include your 5 screenshots]

---

## 🔧 TROUBLESHOOTING

### Issue: "ModuleNotFoundError" during deployment

**Solution**: Check `requirements.txt` has all packages
```
streamlit==1.29.0
pandas==2.1.0
plotly==5.17.0
networkx==3.2
```

### Issue: "FileNotFoundError: data/pbi_association_rules.csv"

**Solution**:
1. Check GitHub repository has `data/` folder
2. Verify all 4 CSV files are in `data/` folder
3. Push again if missing:
   ```bash
   git add data/
   git commit -m "Add data files"
   git push
   ```
4. Redeploy app on Streamlit Cloud

### Issue: App shows but charts don't load

**Solution**: Clear browser cache or try incognito mode

### Issue: Git push asks for username/password repeatedly

**Solution**: Use Personal Access Token as password (see Step 2.6)

### Issue: "Repository not found" on GitHub

**Solution**: Make sure repository is Public, not Private

### Issue: Streamlit Cloud says "App is in a failed state"

**Solutions**:
1. Check deployment logs for specific error
2. Verify Python version compatibility (3.8-3.10)
3. Check all file paths are correct (case-sensitive)
4. Try restarting the app via Streamlit dashboard

---

## 🔄 UPDATING YOUR APP

If you need to make changes:

### Step 1: Edit Files Locally
Make changes to `app.py` or other files

### Step 2: Test Locally
```bash
streamlit run app.py
```

### Step 3: Commit and Push
```bash
git add .
git commit -m "Description of changes"
git push
```

### Step 4: Auto-Deploy
Streamlit Cloud automatically detects changes and redeploys!
(Takes 1-2 minutes)

---

## 📊 MONITORING YOUR APP

### View App Metrics (Streamlit Dashboard)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your app
3. View:
   - Number of visitors
   - App status (running/sleeping)
   - Deployment logs
   - Resource usage

### App Sleep Mode

**Free tier**: App sleeps after 7 days of inactivity
- **What happens**: First visitor after sleep will wait ~30 seconds for app to wake
- **Solution**: Visit your app weekly, or upgrade to paid plan ($20/month for always-on)

---

## 💰 COST BREAKDOWN

| Item | Cost |
|------|------|
| GitHub Account | FREE |
| Git Software | FREE |
| Streamlit Cloud (Community) | FREE |
| Custom Domain (optional) | $12/year |
| Always-On Hosting (optional) | $20/month |

**Total for this assignment**: $0 ✅

---

## ✅ DEPLOYMENT CHECKLIST

**Local Setup:**
- [x] Python installed
- [x] Dependencies installed (`pip install -r requirements.txt`)
- [x] App runs locally (`streamlit run app.py`)
- [x] All features tested

**GitHub:**
- [x] GitHub account created
- [x] Git installed and configured
- [x] Repository created (`mba-dashboard`)
- [x] Code pushed to GitHub
- [x] All files visible on GitHub

**Streamlit Cloud:**
- [x] Streamlit Cloud account created
- [x] App deployed from GitHub
- [x] App URL obtained
- [x] App tested online
- [x] No errors in deployment

**Assignment Documentation:**
- [x] Screenshots captured (5 views)
- [x] URL added to notebook
- [x] Appendix created
- [x] GitHub repo linked
- [x] Features documented

---

## 🎓 ASSIGNMENT SUBMISSION

Include in your submission:

1. **Jupyter Notebook** (`MBA_BreadBasket_Business.ipynb`) with updated section
2. **Live Dashboard URL** (prominently displayed)
3. **GitHub Repository URL** (source code)
4. **Screenshots** (5 different views of the dashboard)
5. **Deployment Documentation** (this guide or summary)
6. **Brief Description** of app features and technology

**Example submission text:**

> This assignment includes a fully deployed interactive web application for
> exploring market basket analysis results. The dashboard enables real-time
> filtering of association rules by support, confidence, and lift thresholds,
> along with interactive visualizations and network graph analysis.
>
> **Live Dashboard**: https://YOUR_USERNAME-mba-dashboard.streamlit.app
> **Source Code**: https://github.com/YOUR_USERNAME/mba-dashboard
>
> The application is hosted on Streamlit Community Cloud (free tier) and
> automatically deployed from GitHub. It demonstrates practical application
> of data mining insights for business decision-making.

---

## 🎉 CONGRATULATIONS!

You have successfully:
✅ Built an interactive data science dashboard
✅ Deployed a web application to the cloud
✅ Created a professional portfolio piece
✅ Completed the assignment requirements
✅ Learned DevOps basics (Git, deployment, hosting)

**Share your dashboard URL with:**
- Your instructor (for grading)
- Classmates (for inspiration)
- LinkedIn (for professional portfolio)
- Future employers (proof of skills)

---

## 📚 NEXT STEPS (Optional Enhancements)

1. **Add Custom Styling**: Modify CSS in `app.py`
2. **Add More Metrics**: Include correlation, conviction details
3. **Time-Based Analysis**: Filter by time of day (if data available)
4. **User Authentication**: Add password protection (Streamlit secrets)
5. **Custom Domain**: Purchase domain and point to app
6. **Analytics**: Integrate Google Analytics
7. **A/B Testing**: Test different layouts with users
8. **Mobile App**: Wrap in React Native or PWA

---

## 🆘 NEED HELP?

**Resources:**
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [GitHub Help](https://docs.github.com)
- [Git Tutorial](https://git-scm.com/doc)

**Common Help Searches:**
- "Streamlit app not deploying"
- "Git push requires password"
- "FileNotFoundError streamlit"
- "How to update deployed streamlit app"

---

**Last Updated**: October 23, 2025
**Version**: 1.0
**Author**: Emmanuel
**Assignment**: Data Mining - Market Basket Analysis

---

**Good luck with your deployment! 🚀**
