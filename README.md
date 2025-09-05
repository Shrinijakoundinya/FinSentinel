# FinSentinel — AI Investor Safety Net (Prototype)

**One-line:** FinSentinel is an AI-powered watchdog that scans suspicious investment messages (WhatsApp/Telegram/SMS/YouTube) and flags likely fraud, pump-and-dump schemes, and unregistered advisories to protect retail investors.

## Problem
Retail investors frequently receive unverified stock tips and investment "advice" on messaging platforms which can lead to severe financial loss. SEBI issues advisories but these are reactive and often miss the instant, viral spread of scam messages.

## Solution (Prototype)
A lightweight web prototype that accepts pasted text (a suspicious message), runs a simple NLP/rule-based classifier (MVP), and returns a risk label with an interpretable rationale. The app demonstrates the core value: early automated detection and investor protection.

## Tech stack
- Frontend: Streamlit (simple UI for demo)
- Backend: Flask (API stub for /analyze endpoint)
- AI: rule-based + small NLP heuristics (placeholder for LLM/NLP models)
- Storage: flat files / simple DB (prototype)

## Demo (quick)
1. Run backend: `python3 app/backend/app.py` (optional for API)
2. Run frontend: `streamlit run app/frontend/streamlit_app.py`
3. Paste a suspicious message (examples in data/samples/messages.txt) and click Analyze.

## How to push to GitHub (one-time steps)
1. Create a new empty repo on GitHub named `FinSentinel` (https://github.com/your-username/FinSentinel)
2. On your machine, run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit — FinSentinel prototype"
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/FinSentinel.git
   git push -u origin main
   ```

## Notes & Next steps
- Replace the rule-based classifier with a trained NLP model or LLM prompts.
- Add multilingual support (Hindi, Telugu, Tamil etc.) via small language models or translation + classifier.
- Add a reporting integration with SEBI/Custodians for verified scam records.

## License
MIT
