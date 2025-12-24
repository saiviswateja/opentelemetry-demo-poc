Local Observability Stack (Alloy + Tempo + Prometheus + Grafana)

This repository provides a local observability setup using Docker Compose.
It uses Grafana Alloy as the OpenTelemetry collector, Tempo for traces, Prometheus for metrics, and Grafana for visualization.

This setup is useful for:

Learning OpenTelemetry

Testing tail-based sampling

Local observability demos or PoCs

Components Used

Grafana Alloy – OpenTelemetry Collector

Tempo – Distributed tracing backend

Prometheus – Metrics storage

Grafana – UI for metrics and traces

Prerequisites

Make sure you have the following installed:

Docker

Docker Compose

Check versions:

docker --version
docker compose version

How to Start the Stack

Run the following command from the repository root:

docker compose up -d


To verify containers are running:

docker compose ps

Exposed Ports and URLs

Grafana UI: http://localhost:3000

Prometheus UI: http://localhost:9090

Tempo API: http://localhost:3200

Alloy UI: http://localhost:12345

OTLP gRPC: localhost:4317

OTLP HTTP: localhost:4318

Grafana Login

Default credentials:

Username: admin
Password: admin

Grafana Datasources

Grafana datasources are auto-provisioned:

Prometheus

Tempo (default)

Enabled features:

Trace to metrics

Trace to service graph

Node graph

TraceQL editor

Prometheus Configuration

Prometheus scrapes metrics from Alloy:

alloy:9464


Remote write receiver is enabled to allow Tempo metrics generator to push metrics into Prometheus.

Tempo Configuration Highlights

OTLP HTTP receiver enabled on port 4318

Local storage backend

Metrics generator enabled:

Span metrics

Service graphs

Trace retention set to 1 hour (for demo purposes)

Sending Traces from an Application

Configure your application to send OTLP traces to:

http://localhost:4318


Example environment variables:

OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf

Viewing Logs

To see Alloy logs:

docker compose logs -f alloy


Alloy runs with debug logging enabled.

Stopping and Cleaning Up

To stop and remove all containers and volumes:

docker compose down -v

Notes

This setup is intended for local development only

Storage is local and not persistent

Retention values are intentionally small

Not recommended for production use
