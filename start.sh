#!/usr/bin/bash

ln -sfn /app/dynamic_programming /app/notebooks/dynamic_programming

conda run -p /opt/conda_env jupyter notebook --notebook-dir=/app/notebooks --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=''

tail -f /dev/null