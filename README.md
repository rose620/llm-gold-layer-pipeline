# Secure LLM Data Pipeline Architecture (Gold Layer Integration)

An end-to-end, production-grade machine learning data pipeline designed to ingest, process, and enrich unstructured text records inside a decoupled enterprise data architecture. 

This repository demonstrates the scalable integration of **Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)** inside a cloud data platform (such as Databricks). It showcases professional workflows for data-agnostic pipelines, runtime adaptive-thinking exception management, and structural credential isolation.

## 🏗️ Architecture Design & Flow
1. **Bronze Layer:** Raw, unstructured textual customer feedback and transactional logs are ingested from production source systems.
2. **Silver Layer:** Data undergoes rigorous structural processing, deduplication, and parsing via native Python ETL libraries to prepare sanitized textual payloads for model consumption.
3. **Gold Layer:** Clean textual streams are passed programmatically to **Claude Haiku 4.5** via the official Anthropic Python SDK to extract deterministic sentiment classifications, core product issues, and corporate action items.

## 🔒 Security & Credential Isolation
Following industry security best practices for open-source distribution and enterprise deployments:
* **Zero Hardcoded Secrets:** Credentials are abstractly managed through system environment variables (`os.getenv`), mimicking a secure cloud configuration layer (e.g., Databricks Secrets or AWS Secrets Manager).
* **Two-Path Isolation Configuration:** Local development utilizes an out-of-repository path structure. Secret configuration tokens are physically separated from the working codebase directory, completely removing exposure risk during Git staging phases.

## 🚀 Key Technical Highlights
* **Adaptive Thinking Exception Handling:** Production runtime logic dynamically loops through model response components to capture textual streams while gracefully bypassing injected `ThinkingBlock` reasoning elements native to modern Claude models.
* **Deterministic Tuning:** Engineered robust system prompts to strictly bind model parsing behaviors, enforcing strict structural uniformity and eliminating structural output variance across bulk datasets.
* **Cost & Latency Optimization:** Architected against the high-efficiency `claude-haiku-4-5-20241022` stable production release line, dramatically reducing token billing scales while processing real-time operational workloads.

## 💻 Local Setup & Execution

### Prerequisites
Install dependencies into your active environment:
```bash
pip install pandas anthropic python-dotenv
```

### Environment Configuration
Export API credential token directly to your active terminal memory session before script invocation:

**Windows PowerShell:**
```powershell
\$env:ANTHROPIC_API_KEY = "sk_ant_key_here"
python main_pipeline.py
```

**Bash / Linux:**
```bash
export ANTHROPIC_API_KEY="sk_ant_key_here"
python main_pipeline.py
```
