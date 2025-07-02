
# GeoWars GPT-4 News Updater

This backend updates geopolitical token news using GPT-4 daily.

## Setup

1. Create a free account on [Render.com](https://render.com/)
2. Deploy this repo as a **Web Service**
3. Set the environment variable `OPENAI_API_KEY` with your OpenAI key
4. Call the `/update` endpoint daily using a cron service (e.g., cron-job.org)

Each call will update:
- `news_irz.json`
- `news_nvbs.json`
- ...
