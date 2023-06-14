# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8
RUN  apt update --fix-missing && apt-get install -y supervisor
COPY . code
WORKDIR /code
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY gunicorncommand.sh code 
RUN chmod +x gunicorn.conf.py
RUN chmod +x /code/gunicorncommand.sh
RUN touch /var/log/application.err.log
RUN touch /var/log/application.out.log
RUN touch /var/log/loaddata.err.log
RUN touch /var/log/loaddata.out.log
RUN chmod +x /code/commands.sh
RUN touch /var/log/dummy.log
EXPOSE 8000
CMD ["/usr/bin/supervisord"]

