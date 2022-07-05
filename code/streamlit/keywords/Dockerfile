FROM python:3.7.10-buster

WORKDIR /usr/src/app

# Arup specific - remove for all commits because it's dumb
RUN curl https://d36u8deuxga9bo.cloudfront.net/certificates/Cisco_Umbrella_Root_CA.cer -o ./Cisco_Umbrella_Root_CA.crt
RUN cp ./Cisco_Umbrella_Root_CA.crt /usr/local/share/ca-certificates/Cisco_Umbrella_Root_CA.crt
RUN update-ca-certificates
RUN pip config set global.cert /etc/ssl/certs/ca-certificates.crt

COPY requirements.txt ./
#COPY .streamlit/config.toml ~/.streamlit/config.toml
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit
EXPOSE 8501
COPY . .
CMD ["streamlit", "run", "keywords.py", "--server.baseUrlPath=/view/ohiocp"]
