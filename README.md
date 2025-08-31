##  Breast Cancer Classification Web App

A clinical-grade, end-to-end machine learning solution that classifies breast cancer tumors as benign or malignant using ensemble modeling techniques and a user-friendly web interface.

###  Project Highlights
- **Full ML pipeline**: data preprocessing with SMOTE, standard scaling, PCA; model tuning via RandomizedSearchCV; ensemble classification.
- **High accuracy & reliability**: Fine-tuned for optimized performance—solid results supporting diagnostic confidence.
- **Production-ready deployment**: Flask-based web app, containerized via Docker, CI/CD enabled on AWS for seamless updates.

###  Evaluation Metrics
- **Accuracy**: *[96%]*  

**Classification Report**  
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0 (Benign)  | 0.97 | 0.97 | 0.97 | 71 |
| 1 (Malignant) | 0.95 | 0.95 | 0.95 | 43 |

**Accuracy**: 0.96  
**Macro Avg**: Precision: 0.96, Recall: 0.96, F1-score: 0.96  
**Weighted Avg**: Precision: 0.96, Recall: 0.96, F1-score: 0.96  

---

###  Tech Stack
| Component            | Technology Used         |
|---------------------|--------------------------|
| Language            | Python 3.10.10               |
| ML Tools            | scikit-learn (SMOTE, PCA, RandomizedSearchCV, Voting Ensemble) |
| Web Framework       | Flask                    |
| Containerization    | Docker                   |
| Deployment          | AWS (CI/CD pipeline)     |
| Visualization       | Seaborn, Matplotlib      |
| Version Control     | GitHub                   |

###  Features
- Intuitive UI for uploading tumor data and receiving predictions.
- Modular architecture for easy maintenance and scalability.
- Incorporates **balanced resampling** (via SMOTE), dimensionality reduction, and ensemble learning for trustworthy outputs.

###  Project Demo
| Interface | Prediction Output |
|-----------|-------------------|
| ![Homepage](images/bc_homepage.png) | ![Prediction](images/bc_prediction.png) |

##  Future Improvements
- **Optimize model accuracy and latency** with transfer learning or neural network techniques.  
- **Containerize with Docker Compose** for multi-service orchestration.  
- **Introduce MLOps pipelines** for model versioning, monitoring, and automatic deployment.  


###  How to Run Locally
```bash
git clone https://github.com/kartheek2003/breast_cancer.git
cd breast_cancer
pip install -r requirements.txt
python app.py
Open your browser at http://127.0.0.1:8000 to interact with the app.

