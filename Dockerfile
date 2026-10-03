FROM python:3.12.7-bookworm

# Set the working directory in the container
WORKDIR /app

COPY . /app

RUN mkdir -p /app/dynamic_programming

# Install wget and other necessary system packages
RUN apt-get update && apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get install -y curl

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/app/.local/bin:$PATH"
ENV VIRTUAL_ENV=/opt/venv

RUN python -m venv /opt/venv

ENV PATH="/root/.local/bin:/opt/venv/bin:$PATH"

RUN poetry lock

RUN poetry install --no-interaction --no-ansi --no-root

# Download Miniconda installer script
# Download the correct Miniconda installer for the container architecture
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "aarch64" ]; then \
        MINICONDA_ARCH="aarch64"; \
    elif [ "$ARCH" = "x86_64" ]; then \
        MINICONDA_ARCH="x86_64"; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${MINICONDA_ARCH}.sh" \
        -O /miniconda.sh

# Install Miniconda
RUN bash /miniconda.sh -b -p /opt/conda

# Add Conda to Path
ENV PATH=/opt/conda/bin:$PATH

# Specify where to create the Conda environment
ENV CONDA_ENV_PATH=/opt/conda_env

# Accept Anaconda Terms of Service
RUN conda tos accept --override-channels \
        --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels \
        --channel https://repo.anaconda.com/pkgs/r

RUN conda create --prefix $CONDA_ENV_PATH python=3.12 -y

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-p", "/opt/conda_env", "/bin/bash", "-c"]

# Install packages from environment.yml into the existing Conda environment
RUN conda env update \
    --prefix /opt/conda_env \
    --file environment.yml

EXPOSE 8888

CMD ["sh", "start.sh"]