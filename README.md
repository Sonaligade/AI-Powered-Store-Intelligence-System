🧠 AI-Powered Store Intelligence System
🚀 Overview

This project builds an end-to-end Store Intelligence System that transforms raw CCTV footage and POS transaction data into actionable business insights. The system combines computer vision, event streaming, real-time analytics, and anomaly detection to help retail stores understand customer behavior, optimize operations, and detect irregularities.

The goal is to simulate a production-grade retail analytics platform capable of working with noisy, real-world data.

🏗️ System Architecture

The system is designed as a modular pipeline:

CCTV Video → Frame Extraction → CV Model → Event Stream → Processing Engine → API → Dashboard
                                     ↘ POS Data Integration ↗
Key Components:
Video Processing Pipeline
Extracts frames from CCTV footage
Detects people and movement using computer vision models
Generates structured events (entry, exit, dwell time, zone activity)
Event Streaming Layer
Converts raw detections into time-stamped event logs
Designed to scale with real-time streaming systems (Kafka-ready)
Data Processing Engine
Merges CCTV events with POS transaction data
Computes:
Footfall trends
Conversion rates (visitors → buyers)
Peak hours
Zone engagement
Anomaly Detection Module
Identifies unusual patterns such as:
High footfall but low sales
Suspicious activity (loitering, crowd spikes)
Operational inefficiencies
Backend API (FastAPI)
Exposes processed insights via REST endpoints
Supports queries for analytics, trends, and anomalies
Interactive Dashboard (Streamlit)
Visualizes:
Footfall vs sales
Time-based trends
Alerts and anomalies
Enables quick decision-making for store managers
🧩 Key Features
📹 Computer Vision Intelligence
People detection from CCTV footage
Zone-based activity tracking
Dwell time estimation
📊 Business Insights
Footfall analytics
Conversion rate calculation
Peak hour detection
Customer behavior trends
⚠️ Anomaly Detection
Rule-based + statistical detection
Highlights mismatches between traffic and revenue
Detects abnormal spikes or drops
🔌 Production-Ready APIs
Clean REST endpoints for integration
Scalable architecture design
📈 Real-Time Ready Design
Event-driven pipeline (can plug into Kafka/Spark)
Designed for horizontal scalability
⚙️ Tech Stack
Computer Vision: OpenCV, YOLO (or similar models)
Backend: FastAPI
Data Processing: Python (Pandas, NumPy)
Streaming (Design-ready): Kafka (conceptual integration)
Dashboard: Streamlit
Storage: CSV / JSON (extensible to databases)
