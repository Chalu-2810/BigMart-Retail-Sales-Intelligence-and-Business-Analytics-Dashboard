# Using This Project on Your Resume & Portfolio

Ready-to-use copy for your resume, LinkedIn, and portfolio site. Adjust the
bracketed details `[ ]` to match your actual experience before using them.

---

## Resume bullet points (pick 3–4 that best match the job description)

**Project title:** BigMart Retail Sales Analytics Dashboard

- Built an end-to-end retail analytics pipeline in Python (Pandas, NumPy)
  that profiled, cleaned, and enriched a 5,681-row retail dataset —
  standardizing inconsistent categorical labels, imputing missing values
  with group-aware statistics, and engineering 4 derived features.
- Designed and shipped a multi-page interactive dashboard with
  **Streamlit + Plotly**, featuring 15+ chart types (treemaps, funnels,
  violin plots, correlation scatter plots with OLS trendlines) across 6
  navigable views with dynamic, cross-filtering sidebar controls.
- Authored a `pytest` suite of 30+ unit tests covering the data-cleaning
  and analytics layers, wired into a GitHub Actions CI pipeline that lints
  (flake8) and tests on every push across 3 Python versions.
- Documented the full analytics workflow (data understanding → cleaning →
  analysis → visualization → insights) in structured Markdown reports,
  demonstrating the standard data-analyst lifecycle end-to-end.
- Containerized the application with Docker and deployed it to Streamlit
  Community Cloud for public access — see live demo link in the README.
- Practiced transparent, defensible analytics: clearly documented a
  synthetic-data assumption in code, docs, and the UI itself rather than
  presenting a fabricated number as real, with reproducible (seeded)
  results and unit tests that pin that reproducibility down.

## One-line portfolio summary

> An interactive retail analytics dashboard (Python · Pandas · Streamlit ·
> Plotly) covering the full pipeline from raw data cleaning to business
> insights, with automated tests and CI.

## Portfolio card description (longer)

A Streamlit dashboard that turns a messy, real-world-style retail dataset
into an executive-ready analytics tool. The project demonstrates the
complete data analyst workflow: understanding and auditing raw data,
cleaning it with reproducible/documented logic, deriving business metrics,
visualizing them with Plotly, and presenting actionable recommendations —
backed by a `pytest` test suite and CI pipeline so the pipeline's
correctness isn't just claimed, it's checked on every commit.

## Talking points for interviews

If asked about this project, be ready to discuss:

1. **Data quality decisions** — *why* you imputed `Item_Weight` per-item
   median (not global mean), and *why* you used `Outlet_Type`-level mode
   for `Outlet_Size` rather than a single global fallback.
2. **The synthetic sales target** — be upfront that the source dataset's
   test split has no real sales column, so you generated a documented,
   seeded proxy to demonstrate the analytics pipeline. Explain you would
   swap in the real `Item_Outlet_Sales` from the official training split
   (or live POS data) in a production setting — the rest of the pipeline
   is unchanged either way. This shows engineering honesty, not a flaw to
   hide.
3. **Testing strategy** — what the 30 tests actually assert (no leftover
   nulls, reproducible randomness, revenue shares sum to 100%, sort order
   is correct) and why those are the right things to test in a data
   pipeline versus, say, testing UI rendering.
4. **What you'd improve with more time** — e.g. swapping in a real ML
   demand-forecasting model, adding a database backend instead of CSV,
   adding outlet-level drill-down, or A/B-testing the dashboard's IA with
   real users.

## Before you publish

- [ ] Replace the Streamlit Cloud demo link placeholder in `README.md`
      with your actual deployed URL.
- [ ] Add 2–3 real screenshots to `assets/` and reference them in the
      README (instructions are in the README's Screenshots section).
- [ ] Update the GitHub repo URL placeholders in `README.md`.
- [ ] If you completed this as part of an internship, keep the internship
      attribution in the README — it adds credibility, not a weakness.
