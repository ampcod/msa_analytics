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

