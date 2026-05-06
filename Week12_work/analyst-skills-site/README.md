# Claude Code — Data Analyst Skills

An interactive reference page showing knowledge worker tasks that Claude Code can automate with a well-connected MCP setup, composed into reusable workflow skills for data analysts.

## Live demo

Deploy via GitHub Pages (see below) or open `index.html` directly in any browser — no build step, no dependencies.

## What's inside

- **9 task categories** — click any card to expand and see individual tasks
- **3 composable skills** — chains of tasks collapsed into single reusable commands:
  - Weekly metrics report
  - Ad-hoc analysis request
  - Data quality audit
- Each skill card shows the full task chain with animated flow indicators, and a **Collapse / Expand** button that animates the chain into a single skill badge

## Deploy to GitHub Pages

1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Under *Source*, select **Deploy from a branch**
4. Choose `main` (or `master`) and `/ (root)`
5. Click **Save** — your site will be live at `https://<your-username>.github.io/<repo-name>/`

## Customise

All data lives in two arrays at the top of the `<script>` block in `index.html`:

- **`CATS`** — task categories with name, accent color, and task list
- **`SKILLS`** — composable skills with name, description, skill color, and the task chips that make up the chain (each chip references a category color)

No framework, no build tooling — just edit and push.
