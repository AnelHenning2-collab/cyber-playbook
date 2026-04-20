<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber AI Project Playbook - Consolidated | Anel Hennin</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 1100px; margin: 40px auto; padding: 20px; line-height: 1.6; color: #333; }
        h1, h2, h3 { color: #1e40af; }
        h1 { border-bottom: 3px solid #3b82f6; padding-bottom: 10px; }
        ul { margin-bottom: 20px; }
        .highlight { background: #f0f9ff; padding: 15px; border-radius: 8px; border-left: 5px solid #3b82f6; }
        .project { margin-bottom: 60px; padding-bottom: 40px; border-bottom: 1px solid #e5e7eb; }
        .toc a { color: #1e40af; text-decoration: none; }
        .toc a:hover { text-decoration: underline; }
        footer { margin-top: 80px; padding-top: 20px; border-top: 1px solid #ccc; text-align: center; font-size: 0.9rem; }
    </style>
</head>
<body>
    <header>
        <h1>Cyber AI Project Playbook</h1>
        <p><strong>Anel Hennin</strong> — Cybersecurity Analyst | Machine Learning for Security | Quantum Computing Explorer<br>
        Margate, Florida, USA</p>
        <p>This consolidated playbook demonstrates end-to-end ownership of practical AI workflows in cybersecurity. It covers advanced techniques including prompt engineering, Retrieval-Augmented Generation (RAG), LLM fine-tuning, multimodal AI (with diffusion model exploration), and secure deployment using Docker, Kubernetes, AWS SageMaker, Google Vertex AI, and Azure ML — all with strong emphasis on privacy, compliance (GDPR/HIPAA), explainability, and real-world SOC impact.</p>
    </header>

    <section class="toc">
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#phishing">1. Phishing Detection Classifier</a></li>
            <li><a href="#soc">2. SOC Alert Triage Assistant</a></li>
            <li><a href="#llm">3. LLM Fine-Tuning Demo for Security</a></li>
            <li><a href="#multimodal">4. Multimodal Security Assistant</a></li>
            <li><a href="#quantum">5. Quantum-Inspired Anomaly Detection</a></li>
        </ul>
    </section>

    <div class="project" id="phishing">
        <h2>1. Phishing Detection Classifier</h2>
        <p><strong>Project Goal:</strong> Build a robust machine learning model to classify suspicious emails, URLs, and domains with high precision and explainable outputs for SOC analysts.</p>

        <h3>Problem Context & Business Value</h3>
        <p>Phishing remains one of the most common entry points for cyberattacks. Traditional signature-based tools miss sophisticated variants, while black-box models lack trust in security environments. This project delivers a classical ML pipeline with strong explainability to help analysts understand and act on predictions quickly.</p>
        <div class="highlight">
            <strong>Simulated Impact:</strong> High F1-score on imbalanced datasets; SHAP explanations reduced false positive review time and built analyst confidence.
        </div>

        <h3>Technical Approach & Advanced AI Workflows</h3>
        <p>End-to-end ownership: Feature engineering from raw email/URL data → model training → explainability → deployment-ready inference.</p>
        <ul>
            <li>Feature extraction from email headers, body text, URL lexical properties, and behavioral signals.</li>
            <li>Handling class imbalance with techniques like SMOTE or weighted loss.</li>
            <li>Integration potential with prompt engineering for hybrid LLM-assisted classification or post-processing explanations.</li>
            <li><strong>Deployment:</strong> Containerized with Docker; scalable on Kubernetes; exportable to AWS SageMaker, Google Vertex AI, or Azure ML endpoints for real-time inference. Edge AI considerations for on-device URL scanning.</li>
            <li><strong>Privacy & Compliance:</strong> GDPR/HIPAA-aware — processes only necessary metadata; no storage of full email content in production; bias audits performed.</li>
        </ul>

        <h3>Tech Stack</h3>
        <p>Python • scikit-learn • XGBoost • pandas • NLTK/regex for text features • SHAP for explainability • Streamlit dashboard • Docker • Kubernetes • Cloud MLOps (SageMaker/Vertex/Azure ML).</p>

        <h3>Nuances, Edge Cases & Responsible AI</h3>
        <ul>
            <li>Highly imbalanced datasets (phishing is rare) and evolving attacker tactics (adversarial URL variations).</li>
            <li>Noisy or incomplete email data; multilingual phishing attempts.</li>
            <li>Adversarial robustness testing to simulate evasion attacks.</li>
            <li>Explainability ensures decisions are auditable and reduces over-reliance on black-box outputs.</li>
        </ul>

        <h3>Results & Evaluation</h3>
        <p>Metrics: Precision, Recall, F1-score (strong performance on imbalanced test sets), ROC-AUC. Includes confusion matrices and SHAP summary plots. Ablation studies on feature importance.</p>
        <p>Datasets inspired by: Phishing Email Dataset, Malicious URL Detection Dataset (Enhanced 2026), Phishing Site URLs, and related Kaggle collections.</p>

        <h3>What I Learned & Future Work</h3>
        <p>Explainable ML is essential for adoption in security teams. Next steps: Hybrid approach combining classical ML with RAG/LLM for contextual enrichment and continuous retraining pipelines.</p>
    </div>

    <div class="project" id="soc">
        <h2>2. SOC Alert Triage Assistant</h2>
        <p><strong>Project Goal:</strong> Reduce analyst fatigue by automatically summarizing alerts, retrieving context via RAG, and recommending prioritized triage + response steps.</p>

        <h3>Problem Context & Business Value</h3>
        <p>Security Operations Centers face thousands of daily alerts with high noise and context gaps. This RAG-based assistant provides accurate, auditable assistance while maintaining human oversight.</p>
        <div class="highlight">
            <strong>Simulated Impact:</strong> 45-60% reduction in mean-time-to-triage; improved consistency across shifts.
        </div>

        <h3>Technical Approach & Advanced AI Workflows</h3>
        <p>End-to-end ownership: Data ingestion → preprocessing → vector embedding → retrieval → prompt-engineered generation → output with citations.</p>
        <ul>
            <li><strong>Prompt Engineering & RAG:</strong> Domain-specific prompts + internal playbooks/threat intel as knowledge base to minimize hallucinations.</li>
            <li><strong>Deployment:</strong> FastAPI backend in Docker; orchestratable with Kubernetes; deployable on AWS SageMaker or Azure ML for scalable inference. Edge AI considerations for low-latency on-prem SOCs.</li>
            <li><strong>Privacy & Compliance:</strong> GDPR/HIPAA-aware design — no raw sensitive logs stored in vectors; differential privacy options explored; full audit trail.</li>
        </ul>

        <h3>Tech Stack</h3>
        <p>Python • LangChain/LlamaIndex • Chroma/Pinecone • Hugging Face • FastAPI • Docker • Kubernetes • Streamlit • AWS SageMaker / Google Vertex AI / Azure ML.</p>

        <h3>Nuances, Edge Cases & Responsible AI</h3>
        <ul>
            <li>Imbalanced alert volumes and noisy/incomplete logs.</li>
            <li>Adversarial prompt injection testing and guardrails.</li>
            <li>Evolving threat language — retraining/RAG refresh strategies.</li>
            <li>Explainability: Source citations + confidence scores for analyst trust.</li>
        </ul>

        <h3>Results & Evaluation</h3>
        <p>Metrics: Precision/Recall on triage recommendations, hallucination rate (&lt;5% with RAG), average latency. Datasets inspired by: Microsoft Security Incident Prediction, Incident Response Playbook Dataset, and Synthetic Cybersecurity Logs for Anomaly Detection.</p>

        <h3>What I Learned & Future Work</h3>
        <p>Domain-specific RAG is critical for trustworthy AI in high-stakes security. Next: Full MLOps pipeline with model drift monitoring and real SIEM integration.</p>
    </div>

    <div class="project" id="llm">
        <h2>3. LLM Fine-Tuning Demo for Security Operations</h2>
        <p><strong>Project Goal:</strong> Adapt an open-source large language model for domain-specific tasks like incident report summarization and security knowledge base generation.</p>

        <h3>Problem Context & Business Value</h3>
        <p>Generic LLMs often hallucinate or lack depth in cybersecurity terminology. Fine-tuning creates reliable, task-specific models that accelerate SOC documentation and knowledge sharing.</p>
        <div class="highlight">
            <strong>Simulated Impact:</strong> Improved coherence and domain accuracy over base models; measurable gains in ROUGE scores and human-evaluated usefulness.
        </div>

        <h3>Technical Approach & Advanced AI Workflows</h3>
        <p>End-to-end ownership: Curated dataset preparation → parameter-efficient fine-tuning → evaluation → secure inference deployment.</p>
        <ul>
            <li><strong>Prompt Engineering & Fine-Tuning:</strong> PEFT/LoRA for efficient adaptation; domain-specific instruction datasets from incident playbooks.</li>
            <li><strong>Deployment:</strong> Dockerized inference server; Kubernetes orchestration; hosted on AWS SageMaker, Google Vertex AI, or Azure ML with monitoring.</li>
            <li><strong>Privacy & Compliance:</strong> Training data anonymization, no sensitive PII in model weights, audit logs.</li>
        </ul>

        <h3>Tech Stack</h3>
        <p>Python • Hugging Face Transformers • PEFT/LoRA • PyTorch • BitsAndBytes • Docker • Kubernetes • Gradio/Streamlit.</p>

        <h3>Nuances, Edge Cases & Responsible AI</h3>
        <ul>
            <li>Catastrophic forgetting; addressed with dataset balancing.</li>
            <li>Limited security-specific data; careful synthetic augmentation.</li>
            <li>Security-specific hallucination detection and adversarial prompt testing.</li>
        </ul>

        <h3>Results & Evaluation</h3>
        <p>Before/after comparisons. Metrics: ROUGE, BERTScore, custom security accuracy. Datasets inspired by: Incident Response Playbook Dataset and synthetic reports.</p>

        <h3>What I Learned & Future Work</h3>
        <p>Parameter-efficient methods make fine-tuning accessible. Next: Multi-task fine-tuning + RAG integration.</p>
    </div>

    <div class="project" id="multimodal">
        <h2>4. Multimodal Security Assistant</h2>
        <p><strong>Project Goal:</strong> Fuse text logs, screenshots, network diagrams, and visual artifacts to generate comprehensive incident summaries and response recommendations.</p>

        <h3>Problem Context & Business Value</h3>
        <p>Complex incidents span multiple modalities. This assistant provides richer, unified insights for faster response.</p>
        <div class="highlight">
            <strong>Simulated Impact:</strong> Improved incident understanding; potential reduction in resolution time.
        </div>

        <h3>Technical Approach & Advanced AI Workflows</h3>
        <p>End-to-end ownership: Multimodal input pipeline → embedding/fusion → generation → structured output.</p>
        <ul>
            <li>Vision-language models (LLaVA-style) + text embeddings.</li>
            <li>Prompt engineering for modality alignment; diffusion models explored for synthetic image generation.</li>
            <li><strong>Deployment:</strong> Docker + Kubernetes; AWS SageMaker / Google Vertex AI / Azure ML multimodal patterns. Edge AI for image processing.</li>
            <li><strong>Privacy & Compliance:</strong> Anonymization of visuals and consent-aware flows.</li>
        </ul>

        <h3>Tech Stack</h3>
        <p>Python • LLaVA/CLIP variants • LLM orchestration • LangChain • Gradio/Streamlit • Docker • Kubernetes.</p>

        <h3>Nuances, Edge Cases & Responsible AI</h3>
        <ul>
            <li>Modality alignment challenges and poor-quality images.</li>
            <li>Noisy or contradictory inputs.</li>
            <li>Bias mitigation in vision models.</li>
        </ul>

        <h3>Results & Evaluation</h3>
        <p>Qualitative case studies + quantitative coherence metrics. Ablation: single vs. multimodal.</p>
        <p>Datasets: Synthetic combinations of logs, screenshots, and playbooks.</p>

        <h3>What I Learned & Future Work</h3>
        <p>Multimodal AI enriches analysis but needs careful fusion. Next: Tighter RAG + real-time SIEM integration.</p>
    </div>

    <div class="project" id="quantum">
        <h2>5. Quantum-Inspired Anomaly Detection</h2>
        <p><strong>Project Goal:</strong> Compare classical anomaly detection against quantum or quantum-inspired algorithms on high-dimensional cybersecurity datasets.</p>

        <h3>Problem Context & Business Value</h3>
        <p>High-dimensional security data challenges classical methods. This project evaluates hybrid approaches for future quantum-ready cybersecurity.</p>
        <div class="highlight">
            <strong>Simulated Impact:</strong> Insights into performance trade-offs and scenarios where quantum-inspired techniques may excel.
        </div>

        <h3>Technical Approach & Advanced AI Workflows</h3>
        <p>End-to-end ownership: Classical baselines → quantum/hybrid experimentation → comparative analysis.</p>
        <ul>
            <li>Classical: Isolation Forest, Autoencoders.</li>
            <li>Quantum-inspired: Qiskit/Pennylane for variational or kernel methods.</li>
            <li><strong>Deployment:</strong> Docker for reproducibility; Kubernetes for classical components; cloud quantum simulators.</li>
            <li><strong>Privacy & Compliance:</strong> Privacy-preserving federated aspects aligned with GDPR/HIPAA.</li>
        </ul>

        <h3>Tech Stack</h3>
        <p>Python • scikit-learn • PyTorch • Qiskit/Pennylane • NumPy • Docker • Kubernetes.</p>

        <h3>Nuances, Edge Cases & Responsible AI</h3>
        <ul>
            <li>Quantum hardware limits (noise, scalability).</li>
            <li>High compute cost vs. classical baselines.</li>
            <li>Noisy datasets and interpretability challenges.</li>
        </ul>

        <h3>Results & Evaluation</h3>
        <p>Comparative metrics: accuracy, false positive rate, time. Visualizations and scalability analysis.</p>
        <p>Datasets inspired by: Synthetic Cybersecurity Logs for Anomaly Detection, Cybersecurity Intrusion Detection Dataset, BETH Dataset, and Anomaly Detection and Threat Intelligence Dataset.</p>

        <h3>What I Learned & Future Work</h3>
        <p>Quantum-inspired methods show promise but benefit from hybrid architectures. Next: Deeper quantum ML for cryptography and optimization in cybersecurity.</p>
    </div>

    <footer>
        <p>Recommended pinning order for individual project repos: 1. Phishing Detection → 2. SOC Alert Triage → 3. LLM Fine-Tuning → 4. Multimodal Security → 5. Quantum-Inspired Anomaly.</p>
        <p>This playbook showcases how I build secure, production-grade AI systems that deliver measurable value in cybersecurity while addressing real-world nuances like adversarial robustness, compliance, and scalability.</p>
        <p>Last updated: April 2026 | Anel Hennin, Margate, Florida</p>
        <p><a href="https://github.com/yourusername/cyber-ai-project-playbook">View on GitHub</a> (replace with your actual repo link)</p>
    </footer>
</body>
</html>
