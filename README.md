# 🚨 FinSentinel — AI Watchdog for Investor Safety  

![FinSentinel Logo](logo.png)

**Team Name:** FinSentinel  
**Hackathon Challenge:** Fraud Prevention (Securities Market Hackathon 2025)  

---

## 🔎 Problem
Retail investors are bombarded daily with unverified stock tips, WhatsApp/Telegram messages, YouTube “advice,” and SMS pump-and-dump schemes.  
These scams spread **faster than SEBI advisories** can react, leading to massive losses for small investors.  

---

## 💡 Solution
**FinSentinel** is an **AI-powered watchdog** that scans suspicious investment messages and flags:  
- Pump-and-dump patterns  
- Unregistered advisories  
- Fraudulent “guaranteed return” claims  

👉 The prototype offers a **simple, lightweight web app**:  
- Paste suspicious text → Get an **instant risk label** + rationale.  
- Protects retail investors with **early warnings** before scams go viral.  

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (lightweight investor-friendly UI)  
- **Backend:** Flask (API stub `/analyze`)  
- **AI/NLP:** Rule-based filters + simple NLP heuristics (expandable to ML/LLMs)  
- **Storage:** Flat files / simple DB (prototype stage)  

---

## 🎯 Key Features
- ✅ **Instant Analysis** of messages (WhatsApp, Telegram, SMS, YouTube comments)  
- ✅ **Risk Labels** (Low / Medium / High) with explainability  
- ✅ **Scam Knowledge Base** for awareness  
- ✅ **Extensible Architecture** → can plug into SEBI APIs in future  

---

## 🚀 Innovation / Differentiator
- **Proactive** → catches scam content at the *message level* (not after damage).  
- **Lightweight & Accessible** → Runs on web, no heavy installs needed.  
- **Scalable** → Can expand to multilingual support (Hindi, Telugu, Tamil, etc.).  
- **Trust-building** → Educates investors while protecting them.  

---

## 📊 Potential Impact & Scalability
- **Impact:** Protect millions of retail investors from fraud, reduce scam-driven losses.  
- **Scalability:** Can scale into a **browser plugin + mobile app**, integrate with SEBI/NSDL/CDSL complaint channels.  

---

## 🖥️ Prototype Demo
### Quick Start
1. Clone repo & install requirements:  
   ```bash
   git clone https://github.com/Shrinijakoundinya/FinSentinel.git
   cd FinSentinel
   pip install -r requirements.txt
