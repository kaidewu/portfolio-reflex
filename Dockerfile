# Stage 1: init
FROM python:3.11 as init

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Create virtualenv which will be copied into the final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Install app requirements and reflex inside virtualenv
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Export static copy of frontend to /app/.web/_static
RUN reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into slim image 
FROM python:3.11-slim
WORKDIR /app
RUN adduser --disabled-password --home /app reflex

# Install Node.js and unzip
RUN apt-get update && apt-get install -y nodejs unzip curl && curl -fsSL https://bun.sh/install | bash

# Copy only the necessary files from the "init" stage
COPY --chown=reflex --from=init /app/.venv /app/.venv
COPY --chown=reflex --from=init /app/requirements.txt /app/requirements.txt
COPY --chown=reflex --from=init /app /app

# Change the ownership and permissions of /app/.local
USER root
RUN mkdir -p /app
RUN chown -R reflex /app
USER reflex

# Activate the virtual environment and install application requirements
ENV PATH="/app/.venv/bin:$PATH"
RUN python3.11 -m venv /app/.venv
RUN /app/.venv/bin/pip install -r /app/requirements.txt

# The following lines are for the specific command for the application.
CMD reflex init && reflex run --env prod