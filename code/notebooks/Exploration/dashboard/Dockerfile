# ODIS Dasboard dockerfile

FROM python:3.9-slim

WORKDIR /home/apps/dashboard

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN git clone --single-branch --branch schema-dev https://github.com/iodepo/odis-arch.git /home/apps/dashboard/odis-arch-git-schema-dev-DO-NOT-TOUCH
RUN git clone --single-branch --branch master https://github.com/iodepo/odis-arch.git /home/apps/dashboard/odis-arch-git-master-DO-NOT-TOUCH

#copy dashboard.py, requirements.txt into /home/apps/dashboard
COPY . .

#install streamlit etc
RUN python -m pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]