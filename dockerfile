FROM apache/airflow:2.7.0

# Installer les dépendances nécessaires
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
