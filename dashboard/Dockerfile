# ODIS Dashboard dockerfile

FROM python:3.9-slim

WORKDIR /home/apps/odis-dashboard

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN git clone --single-branch --branch schema-dev https://github.com/iodepo/odis-arch.git /home/apps/odis-dashboard/odis-arch-git-schema-dev-DO-NOT-TOUCH
RUN git clone --single-branch --branch master https://github.com/iodepo/odis-arch.git /home/apps/odis-dashboard/odis-arch-git-master-DO-NOT-TOUCH

# streamlit-specific commands
RUN mkdir -p /home/apps/odis-dashboard/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /home/apps/odis-dashboard/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
[browser]\n\
gatherUsageStats = false\n\
" > /home/apps/odis-dashboard/.streamlit/config.toml'

#copy dashboard.py, requirements.txt into /home/apps/odis-dashboard
COPY . .

#install streamlit etc
RUN python -m pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]