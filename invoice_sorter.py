import json
import urllib.request

def extract_invoice_data(invoice_text):
    prompt = f"""
    Extract client_name, invoice_date, total_amount, and category as JSON from:
    {invoice_text}
    """
    payload = json.dumps({
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")

    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("response", "{}")
    except Exception as e:
        return f"Local Ollama server status: {e}"

if __name__ == "__main__":
    sample_receipt = "INVOICE #1042 | Date: Oct 17, 2026 | Client: Acme Corp | Total: $450.00"
    print(extract_invoice_data(sample_receipt))
