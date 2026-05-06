# AI Workforce Dynamics Simulator · 2024–2044

An interactive systems dynamics model exploring what happens to employment, productivity, and inequality as AI agents enter the workforce. Adjust four parameters and get historically-grounded scenario analysis — no server required, no API calls, fully static.

## What it does

- **Four sliders**: Adoption Speed, Sector Exposure, Policy Response, Safety Net
- **Four live charts**: Agent penetration S-curve, Employment index, Productivity index, Inequality index
- **Eight scenario archetypes**: each with 2–3 detailed historical analogies
- **Per-parameter historical notes**: every combination of slider values maps to a specific historical parallel
- **625 possible parameter combinations** covered through scenario + dimension lookup

## Scenarios covered

| Scenario | Trigger conditions |
|---|---|
| Disruption Unchecked | High adoption + low policy + high exposure |
| Managed Transition | High adoption + high policy |
| Cautious Innovation | Low adoption + strong safety net or policy |
| Gradual Drift | Low adoption + low policy |
| Fast & Fragmented | High adoption + moderate policy |
| Polarization Risk | High exposure + weak redistribution |
| Baseline Path | Moderate everything |

## Deploying to GitHub Pages

### Option 1: New repository (fastest)

```bash
# Create a new repo on GitHub, then:
git init
git add index.html README.md
git commit -m "initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Then in your repo: **Settings → Pages → Source: Deploy from a branch → Branch: main → / (root) → Save**

Your site will be live at `https://YOUR_USERNAME.github.io/YOUR_REPO`

### Option 2: Existing repository

Copy `index.html` into the repository root (or a `/docs` folder if you prefer), configure GitHub Pages to serve from that location.

### Option 3: Any static host

The file is a single self-contained `index.html`. It works on:
- **Netlify**: drag and drop the file at netlify.com/drop
- **Vercel**: `vercel --prod` from the project folder
- **Cloudflare Pages**: connect repo or upload directly
- **Any web server**: copy to document root

## External dependencies (CDN, loaded at runtime)

- [Chart.js 4.4.1](https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js) — charts
- [Google Fonts](https://fonts.googleapis.com) — Fraunces, DM Sans, JetBrains Mono

No build step. No npm. No bundler. Open `index.html` directly in a browser to run locally.

## Model notes

The simulation uses an S-curve (logistic function) for agent penetration, with four derived variables:

- **Penetration**: logistic curve with inflection point determined by adoption speed
- **Employment**: starts at 100, declines by sector exposure × penetration, partially recovered by policy and safety net
- **Productivity**: grows with penetration, amplified by sector exposure
- **Inequality**: rises with penetration × exposure, moderated by policy and safety net strength

All values are indices, not absolute figures. The model is calibrated against historical comparables (Frey & Osborne automation estimates, Acemoglu & Restrepo displacement-reinstatement framework, Autor task-biased change literature).

**This is not a forecast.** It is a scenario exploration tool designed to make the parameter space of technological transitions legible and historically situated.

## Academic references

- Acemoglu, D. & Restrepo, P. (2022). *Tasks, Automation, and the Rise in US Wage Inequality*
- Autor, D., Levy, F. & Murnane, R. (2003). *The Skill Content of Recent Technological Change*
- Autor, D., Dorn, D. & Hanson, G. (2013). *The China Syndrome*
- Brynjolfsson, E. & McAfee, A. (2014). *The Second Machine Age*
- Frey, C.B. & Osborne, M.A. (2013). *The Future of Employment*
- Goldin, C. & Katz, L. (2008). *The Race Between Education and Technology*
- Milanovic, B. (2016). *Global Inequality: A New Approach for the Age of Globalization*
