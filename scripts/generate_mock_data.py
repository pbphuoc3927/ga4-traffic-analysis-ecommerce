import pandas as pd
import random
from datetime import datetime, timedelta

# Cấu hình
NUM_ROWS = 1000
OUTPUT_PATH = r"C:\Users\phuoc\ga4-traffic-analysis-ecommerce\data\traffic_data.csv"

# Các lựa chọn giả lập
sources = ['google', 'facebook', 'tiktok', 'instagram', 'direct', 'zalo', 'email']
mediums = ['organic', 'paid', 'referral', 'direct']
devices = ['mobile', 'desktop', 'tablet']
countries = ['Vietnam', 'Thailand', 'Indonesia', 'Philippines', 'Malaysia']

# Hàm sinh ngày ngẫu nhiên trong 30 ngày gần nhất
def random_date():
    start_date = datetime.now() - timedelta(days=30)
    return start_date + timedelta(days=random.randint(0, 30))

# Tạo dữ liệu
data = []
for _ in range(NUM_ROWS):
    timestamp = random_date().strftime("%Y-%m-%d")
    source = random.choice(sources)
    medium = random.choice(mediums)
    device = random.choice(devices)
    country = random.choice(countries)
    sessions = random.randint(1, 3)
    conversions = random.choices([0, 1], weights=[0.7, 0.3])[0]
    revenue = conversions * random.choice([0, 190000, 250000, 320000, 450000])

    data.append([
        timestamp, source, medium, device, country, sessions, conversions, revenue
    ])

# Ghi vào CSV
df = pd.DataFrame(data, columns=[
    'timestamp', 'source', 'medium', 'device_category', 'country',
    'sessions', 'conversions', 'revenue'
])
df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Đã tạo {NUM_ROWS} dòng dữ liệu mock vào: {OUTPUT_PATH}")
