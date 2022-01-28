FROM ubuntu:18.04 AS installer-env

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    cron \
    ca-certificates \
    netbase \
    python3 \
    python3-pip \
    python3-setuptools \      
    postgresql \
    python-psycopg2 \
    libpq-dev \        
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

# run this once every hour Monday-Friday
RUN echo "0 * * * 1-5 cd /usr/src/app && python3 /usr/src/app/getotclist.py >> /var/log/cron.log 2>&1" > /etc/cron.d/root
RUN echo "0 8 * * 0 echo '' > /var/log/cron.log" >> /etc/cron.d/root
# cron needs a blank line
RUN echo "" >> /etc/cron.d/root

# Apply cron job
RUN chmod +x /etc/cron.d/root
RUN crontab /etc/cron.d/root

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

# docker run -itd --network="host" otc