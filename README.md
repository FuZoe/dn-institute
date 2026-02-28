Distributed Networks Institute (DNI) aims to help infrastructure resilience and financial health of distributed networks through scientific, engineering, and educational efforts. We are a part of a 501(c)3 non-profit incubator in Washington, DC called [BlockShop](https://blockshop.org/). Constantly on the lookout for talent, we encourage anyone to contribute code, market analysis, and engineering expertise to one of our [active projects](https://dn.institute/#projects). Multiple research grants and [code bounties](https://github.com/1712n/dn-institute/labels/%F0%9F%92%B0%20bounty) are available.

## � PD-Hunter Intelligence (PDHI)

**[📊 Live Dashboard](https://fuzoe.github.io/dn-institute/dashboard.html)** | Real-time AI-enriched tactical insights for ProjectDiscovery bounties

### Features

- **Hunter Cards** - Each bounty displays Technical Hint, Bounty Amount, and Friction Level
- **S-Tier Highlighting** - High-value bounties (like the $1.2k TLSX issue) are prominently featured
- **Expert Intelligence** - Curated hints preserved across updates, AI-generated for new issues
- **Auto-Refresh** - Data pipeline runs every 6 hours via GitHub Actions

### How It Works

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  GitHub Issues  │────▶│  Go Scraper      │────▶│  bounty_issues  │
│  (PD Repos)     │     │  fetch_bounty_   │     │  .json          │
└─────────────────┘     │  issues.go       │     └────────┬────────┘
                        └──────────────────┘              │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  index.html     │◀────│  Python Enricher │◀────│  GPT-4o AI      │
│  (Dashboard)    │     │  enrich_bounties │     │  (new issues)   │
└─────────────────┘     │  .py             │     └─────────────────┘
                        └──────────────────┘
                               │
                               ▼
                        Expert Hints are
                        PRESERVED for
                        existing issues
```

### Automation Pipeline

The `.github/workflows/update_bounties.yml` workflow:

1. **Triggers** every 6 hours + manual dispatch
2. **Scrapes** latest bounty issues from ProjectDiscovery repos
3. **Enriches** with AI analysis (preserving existing expert hints)
4. **Updates** the dashboard with fresh data
5. **Commits** changes back to the repository

### Local Development

```bash
# Fetch latest issues
go run fetch_bounty_issues.go

# Enrich with AI (requires GITHUB_TOKEN)
python enrich_bounties.py

# Update dashboard
python update_dashboard.py

# Preview
python -m http.server 8080
```

## �🏆 Challenge Program

[![Challenge Program Video](https://blockshopdc.com/static/assets/images/challenge.jpg)](https://link.hygge.work/MayaVick_Challenge)

We maintain a list of real-world problems we work on to give interested individuals a chance to prove themselves, learn a bit about us, and boost their GitHub profiles in the process. The challenge program was so successful for some teams, that they made solving a challenge a hard requirement for joining them. Our challenges are extremely independent and will require you to manage your own time and work process. Check out the [success stories](https://www.instagram.com/explore/tags/challenge_successstory/) of the challenge winners.

### General rules

- Anyone can participate in a challenge. You do not need anyone's approval to start working or to submit your results.
- Some challenges are paid and have bounties attached to them. When you complete a bounty task, please message bounty-payout@dn.institute with a link to your merged pull request and a Bitcoin or an altcoin address to get paid. We pay all bounties at the end of each month and close tasks as soon as we get enough good quality submissions that fulfill all the requirements.
- By participating in the Challenge Program, you agree to let challenge creators use any and all work submitted for any internal or external purposes.

### Navigating and Working with the Tasks

- In the [issue list](https://github.com/1712n/dn-institute/issues), you'll find a list of tasks that are currently available.
- You are free to start working on any open challenge issue whenever you want.
- For highly complex tasks, we are willing to lock individual issues for qualified candidates to make sure no one else is working on it. For that, please comment in the issue and email challenge@blockshop.org with your CV/profile. We'll review your request and assign the issue exclusively to you.
- To be alerted whenever we create new tasks, please click "👁 Watch" and "☆ Star" in the upper right corner.

## 🌱 Giving Back

### 🔬 Research

DNI has a growing scientific research team, focused on the application of Large Language Models to risk modeling. If you are interested in gaining relevant skills while publishing scientific papers along the way, solve one of the [NLP challenges](https://github.com/1712n/dn-institute/labels/nlp) and mention your interest in joining the research team. Multiple research grants are available!

### 🧑‍🎓 Training

We are happy to train anyone willing to learn our tools. Show initiative by contributing to one of the [open issues](https://github.com/1712n/dn-institute/issues) and mention in your pull request that you want to be considered for any training opportunities they might have available.

### 🎖️ Veterans

Our diverse community includes military veterans from a wide variety of backgrounds. If you are in the process of getting out of the U.S. military, check out our SkillBridge program. Whether you qualify as eligible U.S. military personnel, or served in the armed forces of another country, solve one of the challenges and/or reach out to [@jhirschkorn](https://github.com/jhirschkorn).
