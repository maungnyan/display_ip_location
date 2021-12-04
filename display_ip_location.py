import subprocess
import re


def get_ip():
    # Acquire IP by using curl
    try:
        raw_result = subprocess.check_output(["curl", "https://api.ipify.org", "-s"]).decode()
        check_ip = re.search(r"\d{1,255}\.\d{1,255}\.\d{1,255}\.\d{1,255}", raw_result)
        return (check_ip.group(0).strip())  # remove whitespaces if any
    except:
        return False


def get_location(ip_result):
    # Acquire location based on IP by using geoiplookup
    try:
        raw_result = subprocess.check_output(["geoiplookup", ip_result]).decode()
        ip_location = re.search(r":(.*)", raw_result)
        return (ip_location.group(1).strip())  # remove whitespaces if any
    except:
        return False


if __name__ == '__main__':
    ip_result = get_ip()
    if ip_result:
        ip_location = get_location(ip_result)
        if ip_location:
            print(ip_result + " : " + ip_location)
