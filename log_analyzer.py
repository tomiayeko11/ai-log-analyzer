import os
import ollama

raw_firewall_logs = """
2026-07-31 10:14:22 UTC - INFO - User admin logged in successfully from 192.168.1.5
2026-07-31 10:15:01 UTC - WARN - Failed login attempt for user root from 203.0.113.42
2026-07-31 10:15:02 UTC - WARN - Failed login attempt for user root from 203.0.113.42
2026-07-31 10:15:03 UTC - WARN - Failed login attempt for user root from 203.0.113.42
2026-07-31 10:15:04 UTC - WARN - Failed login attempt for user root from 203.0.113.42
2026-07-31 10:15:05 UTC - WARN - Failed login attempt for user root from 203.0.113.42
2026-07-31 10:16:10 UTC - INFO - User service_account logged in from 10.0.0.15
"""
system_prompt = (
	"You are an expert Cybersecurity Incident Response AI. Analyze the following raw "
    "authentication logs. Identify any security anomalies, specifically checking for "
    "brute-force indicators or unauthorized access patterns. Output your findings as a "
    "clean, structured markdown report summarizing the threat level and recommended mitigation steps."
)

full_prompt = f"{system_prompt}\n\n### RAW LOG DATA:\n{raw_firewall_logs}"

print("🤖 [Status] Initializing local privacy-safe security model (Llama 3.1)...")

try:
	response = ollama.generate(model='llama3.1:8b', prompt=full_prompt)
	analysis_results = response['response']

	output_filename = "security_threat_alert.md"
	with open(output_filename, "w") as report_file:
	    report_file.write(analysis_results)

	print(f"✅ [Success] Analysis complete! Threat report generated at: {output_filename}")

except Exception as e:
	print(f"❌ [Error] Failed to connect to local model. Ensure Ollama is running. Details: {e}")


