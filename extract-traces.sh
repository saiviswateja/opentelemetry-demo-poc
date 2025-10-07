#!/bin/bash

# Script to extract traces from Alloy logs and save to file

OUTPUT_FILE="traces/extracted-traces.txt"

echo "Extracting traces from Alloy logs..."
echo "=========================================" > "$OUTPUT_FILE"
echo "Traces extracted at: $(date)" >> "$OUTPUT_FILE"
echo "=========================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Extract trace information from docker logs - look for actual trace data
docker logs alloy 2>&1 | grep -E -A 30 "(ResourceSpans #0|msg=Traces|database-query|grpc-demo-service)" >> "$OUTPUT_FILE"

echo "Traces extracted to: $OUTPUT_FILE"
echo "Total trace entries found: $(grep -c -E "(ResourceSpans|Span #|traces)" "$OUTPUT_FILE")"
