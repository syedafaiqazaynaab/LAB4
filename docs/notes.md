# Lab 4 Notes: Python Environments

## 1. Comparing Python Environments

| Feature | pip | venv | Conda |
|---|---|---|---|
| Purpose | Installs Python packages | Creates an isolated Python environment | Manages environments and packages, including non-Python dependencies |
| Main command | `pip install numpy` | `python -m venv venv` | `conda create --name demo python=3.11` |
| Best use | Installing libraries | Keeping project dependencies separate | Managing environments and packages, including non-Python dependencies |

## 2. When to Use Google Colab vs Local Jupyter

Google Colab is useful when I want to run notebooks online without installing Python packages locally, and it can provide access to GPUs. Local Jupyter is useful when I want to work with files on my computer and use a project-specific Python environment.

## 3. Python Version

Python version: 3.11.17 (Conda demo environment)
