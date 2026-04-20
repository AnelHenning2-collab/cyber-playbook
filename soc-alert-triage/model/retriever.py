def retrieve_context(text: str):
    text = text.lower()

    if "failed login" in text:
        return "Authentication failure / brute force attempt"
    if "malware" in text:
        return "Possible malware execution"
    if "ransom" in text:
        return "Ransomware behavior detected"
    if "port scan" in text:
        return "Reconnaissance / scanning activity"

    return "General suspicious activity"
