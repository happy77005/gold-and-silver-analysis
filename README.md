Gold & Silver Price Analysis (2018–2023)
🔹 Overview
This project analyzes 5 years of historical gold and silver price data (2018–2023), exploring long-term trends and statistical relationships between the two commodities.

In addition to traditional batch analysis, the project also simulates a real-time streaming pipeline — consuming historical data row by row with artificial delays to mimic live data feeds. This allows us to experiment with concepts from real-time data engineering (Kafka/Spark Streaming) without the need for heavy infrastructure.

🔹 Features
Batch Analysis

Cleaned and preprocessed historical gold & silver datasets.

Conducted statistical correlation analysis using Karl Pearson’s coefficient.

Visualized long-term price trends using matplotlib.

Streaming Simulation

Replayed historical data with a delay (time.sleep) to simulate a live price feed.

Processed each incoming record in “streaming mode.”

Plotted real-time updates to visualize dynamic data flow.

🔹 Key Learnings
Difference between batch processing (full dataset at once) and stream processing (row-by-row).

Simulated the role of Kafka producers/consumers by generating incremental events from CSV files.

Built a minimal proof-of-concept pipeline showing how financial time-series data can be analyzed both historically and in real-time.

🔹 Tech Stack
Languages: Python (Pandas, NumPy)

Visualization: Matplotlib

Concepts: Batch vs. Streaming, Correlation Analysis, Real-time Data Simulation

🔹 Future Extensions
Replace simulated stream with a real Kafka producer/consumer setup.

Scale the pipeline to process multiple commodity feeds in parallel.

Integrate with cloud-based data warehouses (AWS Kinesis, GCP Pub/Sub).
