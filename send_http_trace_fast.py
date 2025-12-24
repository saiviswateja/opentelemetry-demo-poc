#!/usr/bin/env python3

import time
import json
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

# Set up the tracer
resource = Resource.create({
    "service.name": "http-demo-service-fast",
    "service.version": "3.0.1",
    "deployment.environment": "development"
})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

# Configure OTLP HTTP exporter
otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4318/v1/traces"
)

# Add the exporter to the tracer
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create and send a trace
print("Sending HTTP trace (fast)...")

with tracer.start_as_current_span("database-query-http") as span:
    span.set_attribute("db.system", "postgresql")
    span.set_attribute("db.name", "user_database")
    span.set_attribute("db.operation", "SELECT")
    span.set_attribute("db.table", "users")
    span.set_attribute("internal.force_sample", "fs:1")
    
    # Simulate fast query - well under 5 second latency threshold
    print("⚡ Simulating fast database query (100ms)...")
    time.sleep(0.1)
    
    # Add detailed attributes
    span.set_attribute("query.duration_ms", 100)
    span.set_attribute("query.rows_affected", 3)
    span.set_attribute("connection.pool.size", 10)
    span.set_attribute("slow_query", False)
    
    print("✅ HTTP trace sent successfully (fast - will NOT be sampled unless service name matches)")

# Force flush to ensure the trace is sent
trace.get_tracer_provider().force_flush(timeout_millis=5000)
print("🚀 Trace export completed!")

