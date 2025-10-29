# MLOPS-1-DVC-DataVersion 🚀

> **First Project in the MLOps Learning Series**  
> *Mastering Data Version Control with Git + DVC*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/DVC-3.0%2B-945DD6)](https://dvc.org/)
[![AWS S3](https://img.shields.io/badge/AWS-S3-orange)](https://aws.amazon.com/s3/)

---

## 📋 Project Overview

This project demonstrates how to version control datasets using **Git + DVC (Data Version Control)**, a foundational skill in the MLOps lifecycle. It's part of my journey to build robust, reproducible machine learning systems from the ground up.

**What you'll learn:**
- 🗂️ Version control for large datasets (without bloating Git repositories)
- ☁️ Remote storage configuration with Amazon S3
- 🔄 Reproducible data pipelines
- 📊 Track multiple versions of datasets efficiently

This is the **first step** in my MLOps series, focusing on data versioning before diving into experiment tracking, model management, and CI/CD automation.

---

## 🏗️ Project Structure

```
MLOPS-1-DVC-DataVersion/
│
├── data/              # CSV data folder (tracked by DVC)
├── mycode.py          # Python script to generate/modify data
├── data.dvc           # DVC tracking file for data/
├── .dvc/              # DVC metadata
├── .dvcignore         # Files to ignore in DVC
├── .gitignore         # Files to ignore in Git
└── README.md          # This file
```

---

## 🔧 Technologies & Tools

- **Languages:** Python
- **Version Control:** Git, DVC
- **Cloud Storage:** AWS S3
- **Package Management:** pip, Poetry/uv

---

## 🚀 Workflow Summary

### 1. Initialize Git and DVC
```bash
git init
pip install dvc[s3]
dvc init
```

### 2. Create and commit initial data
```bash
mkdir data
python mycode.py
git add .
git commit -m "Initial commit: code and data"
git push origin main
```

### 3. Configure DVC Remote (Amazon S3)
```bash
dvc remote add -d myremote s3://dvc-github-test/data
git add .dvc/config
git commit -m "Configured DVC remote to S3"
git push
```

### 4. Let DVC manage the data folder
```bash
# Start tracking data with DVC
dvc add data/

# Stop tracking data with Git
git rm -r --cached data

# Commit DVC tracking files
git add .gitignore data.dvc
git commit -m "Track data with DVC"

# Push data to S3
dvc commit
dvc push

# Push metadata to Git
git add .
git commit -m "Data version 1"
git push
```

### 5. Update data and create new versions
Each time you modify the data:

```bash
python mycode.py          # Modify your data
dvc status                # Check what changed
dvc commit                # Save changes to DVC
dvc push                  # Upload to S3
git add .                 # Stage DVC metadata
git commit -m "Data version X"  # Commit to Git
git push                  # Push to GitHub
```

---

## 📚 Key DVC Commands

| Command | Description |
|---------|-------------|
| `dvc init` | Initialize DVC in the project |
| `dvc add data/` | Start tracking the `data/` folder with DVC |
| `dvc remote add -d myremote s3://...` | Add remote storage (S3, GDrive, etc.) |
| `dvc push` | Upload dataset to the remote storage |
| `dvc pull` | Download dataset from the remote storage |
| `dvc commit` | Save new changes to DVC-tracked files |
| `dvc status` | Check synchronization between workspace and remote |
| `dvc remote modify myremote url ...` | Change the remote URL |
| `dvc remote list` | Show all configured DVC remotes |

---

## 🔄 Reproducing Any Data Version

One of DVC's superpowers is **perfect reproducibility**. You can go back to any data version at any time:

```bash
git checkout <commit_hash>
dvc pull
```

This downloads the exact dataset used at that commit, making your experiments fully reproducible.

---

## 🌱 Learning Notes

- **DVC acts like "Git for data"**: It stores only metadata and checksums in Git, while the actual data lives in S3 (or any other remote storage).
- **Lightweight repositories**: Your Git repo stays small because large files never touch it.
- **Foundation for MLOps**: This project sets the stage for experiment tracking, model versioning, and automated pipelines.

---


## 👨‍💻 About Me

**Jorge** | Software Developer & Data Scientist  
📍 Based in Lyon, France  
🧠 Passionate about AI, machine learning, and building robust software systems  
🌱 Currently building Generative AI from scratch and diving deep into Software Architecture

### Connect with me:
- [LinkedIn](https://linkedin.com/in/jorballcor)
- [Website](https://jorballcor.github.io)
- [Email](mailto:jorge.ballcor@gmail.com)

---

## 🏷️ Tags

`MLOps` `DVC` `Data-Versioning` `Git` `AWS` `S3` `Machine-Learning` `Python` `Reproducibility` `Data-Science`

---

## 📝 License

This project is part of my learning journey and is available for educational purposes.

---

⭐ **If you find this project helpful, consider giving it a star!**
