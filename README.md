# 🌍 MSA Analytics Platform for ESG Risk Evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-PostGIS-brightgreen?logo=postgresql)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey?logo=flask)
![LLM](https://img.shields.io/badge/LLM-Ollama%20LLaMA3.2-orange?logo=llama)
![Status](https://img.shields.io/badge/Status-Active-informational)

## 🧠 Overview

This project is an end-to-end platform for **Mean Species Abundance (MSA) analytics** focused on spatial biodiversity assessment in support of **ESG (Environmental, Social, Governance)** compliance. It utilizes spatial queries, real-time geospatial analytics, interactive mapping, and LLM-based chatbot guidance to assist industries and policymakers in assessing ecological degradation risks.

It integrates:
- 🗺️ Geospatial analysis via PostgreSQL + PostGIS
- 📊 Visualization via Leaflet.js & Looker Studio
- 🔎 MSA queries using a Flask API
- 🤖 RAG-based chatbot for ESG standard interpretation (ESRS E4 etc.)

---

## ✨ Key Features

- 🔍 **MSA Radius Query Engine**: Returns average MSA within a 3 km buffer from input coordinates.
- 📍 **Interactive Germany Map**: Add facility markers and view risk reports.
- 🐘 **Spatial PostgreSQL (PostGIS)**: Stores georeferenced MSA data across 1995, 2010, 2015, 2020.
- 🧾 **BI Reports**: Visual dashboards analyzing CO₂ emissions across 4 industrial sectors.
- 🤖 **Chatbot Assistant**: Ollama + LLaMA3.2 based chatbot for ESRS & biodiversity compliance help.
- 📦 **Docker-ready Architecture**: Future-ready for scaling and cloud hosting.

---

## 🌐 Technologies Used

| Layer        | Tech Stack                              |
|--------------|------------------------------------------|
| Backend      | Flask (Python)                          |
| Database     | PostgreSQL + PostGIS                    |
| Frontend     | HTML, CSS, JavaScript, Leaflet.js       |
| BI Reports   | Google Looker Studio                    |
| AI Chatbot   | Ollama LLaMA 3.2 + local PDF KB         |
| Geocoding    | OpenCage API                            |

---

## 🗂️ Dataset Sources

- 🌿 [GLOBIO](https://www.globio.info/globio-web-explorer) – MSA by land-use
- 🌍 [Copernicus EU](https://land.copernicus.eu) – Land Cover & Spatial layers
- ☁️ [Climate TRACE](https://climatetrace.org) – Industrial Emissions

## Images
### Coordinate based Analysis
<img width="1894" height="1041" alt="Screenshot 2025-05-12 131511" src="https://github.com/user-attachments/assets/a99346fa-811c-4bd9-9a6c-ac1f29fb8b66" />

### BI Reports
<img width="1688" height="966" alt="Screenshot 2025-04-11 101123" src="https://github.com/user-attachments/assets/96c7513c-d8e5-4b45-a92a-2e372f0312c9" />
<img width="1196" height="897" alt="Screenshot 2025-04-13 131618" src="https://github.com/user-attachments/assets/b689e1d8-1c91-4591-9cfa-3ecd63aaa3de" />



### Chatbot
<img width="771" height="942" alt="Screenshot 2025-04-08 232959" src="https://github.com/user-attachments/assets/616b897d-dab0-4a4f-a58d-4a950e719ea0" />

