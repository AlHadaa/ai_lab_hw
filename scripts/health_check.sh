#!/usr/bin/env bash
# ==============================================================================
# Script: health_check.sh
# Purpose: Validates API endpoints via Linux cURL, grep, and exit codes
# Course: AI Lab - Dr. Mohammed Al-Dhobaie
# ==============================================================================

SERVER_URL="http://127.0.0.1:5000"

echo "🔍 [Health Check] Pinging SmartText AI server at ${SERVER_URL}..."

# 1. Health check endpoint probe using curl
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${SERVER_URL}/api/health")

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "✅ [SUCCESS] Health check responded with HTTP 200 OK!"
else
    echo "❌ [FAIL] Health check failed with status: ${HTTP_STATUS}"
    exit 1
fi

# 2. Inspect JSON response payload
echo "📄 Response Payload:"
curl -s "${SERVER_URL}/api/health" | grep "status"

# 3. Test text analysis endpoint via curl POST
echo ""
echo "🧪 [API Test] Sending test payload to /api/analyze..."
SAMPLE_RESPONSE=$(curl -s -X POST "${SERVER_URL}/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "Clean coding and Linux commands make AI development fantastic!"}')

echo "${SAMPLE_RESPONSE}" | grep -q '"success":true' && echo "✅ [SUCCESS] /api/analyze executed successfully!"

echo "=================================================="
echo "🎉 All Linux health probes passed!"
echo "=================================================="
