# MemShield

Detects malware from computer memory snapshots using machine learning.

## Objective

Malware behaves differently from normal programs in memory. MemShield analyzes 55 memory activity features extracted from system memory dumps and classifies them as **benign or malicious** using Logistic Regression.

## Dataset

**CIC-MalMem-2022** — Canadian Institute for Cybersecurity  
- 58,596 memory dump records  
- 55 numerical features extracted from real-world malware samples  
- Classes: Benign, Ransomware, Spyware, Trojan Horse  
- Balanced dataset: 50% benign, 50% malicious  

## Results

| Metric | Score |
|---|---|
| Training Accuracy | 97.1% |
| Testing Accuracy | 97.1% |
| False Negatives (missed malware) | 22 |
| False Positives (false alarms) | 148 |
