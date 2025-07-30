# GA4 Traffic Breakdown for E-commerce

A Python-based project that simulates and analyzes Google Analytics 4 (GA4) traffic data for an e-commerce business. The goal is to generate actionable insights on acquisition channels, user devices, and revenue performance.

---

## 📌 Objective

- Simulate realistic GA4 traffic data for an e-commerce website.
- Analyze traffic by source, medium, device, and geography.
- Identify patterns in sessions, conversions, and revenue.
- Deliver insights to guide data-driven marketing decisions.

---

## 📁 Dataset Description

The data is synthetically generated to reflect typical e-commerce GA4 tracking.

| Column           | Description                                  |
|------------------|----------------------------------------------|
| `timestamp`      | Date of the session                          |
| `source`         | Traffic source (e.g. google, facebook)       |
| `medium`         | Acquisition medium (e.g. cpc, organic)       |
| `device_category`| Device type used by the visitor              |
| `country`        | Visitor's country                            |
| `sessions`       | Number of sessions                           |
| `conversions`    | Number of conversions                        |
| `revenue`        | Revenue generated from that visit            |

- Data file: `data/mock_ga4_data.csv`  
- Data generation script: `scripts/generate_mock_data.py`

---

## ❓ Key Business Questions

- Which traffic sources and mediums drive the most conversions?
- Which devices and countries bring in the most revenue?
- What is the conversion rate and revenue per session by channel?
- Which sources are high in traffic but low in performance?

---

## 🧰 Tech Stack

- **Language**: Python 3.10+
- **Environment**: Jupyter Notebook
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `faker`

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/pbphuoc3927/ga4-traffic-analysis-ecommerce.git
cd ga4-traffic-analysis-ecommerce
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dataset

```bash
python scripts/generate_mock_data.py
```

### 4. Open and run the notebook

```bash
jupyter notebook notebooks/ga4_traffic_analysis.ipynb
```

---

## 📈 Key Insights

* **Google (organic)** and **Facebook (CPC)** were top-performing channels in terms of both sessions and conversions.
* **Tablet users** showed the highest conversion rate, though traffic volume was lower.
* The **United States** contributed the highest revenue per session.
* Channels such as `referral` had high traffic but poor conversion performance.

---

## ✅ Recommendations

* **Reallocate ad budget** from underperforming referral traffic to high-performing CPC campaigns.
* **Optimize mobile experience** to improve conversion from mobile traffic, which dominates overall sessions.
* **Target tablet users more effectively**, as they demonstrate strong intent to purchase.
* **Focus on high-ROI geographies**, particularly the United States, in future campaigns.

---

## ✍️ Author

**\Pham Ba Phuoc**
Created for the Marketing/Data Analyst Portfolio – Q3 2025

---

## 📌 Status

✅ Project completed
📊 Dataset and analysis hosted in this repository
📁 Notebook: `notebooks/ga4_traffic_analysis.ipynb`
