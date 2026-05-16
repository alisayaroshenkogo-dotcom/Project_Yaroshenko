"""
В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
(например, в URL-apece http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
домен выделен полужирным)
"""
import re

def extract_domains(filename):
    with open("radio_stations.txt", 'r', encoding='utf-8') as file:
        pattern = r'https?://([a-zA-Z0-9.-]+)'
        domains = [match for line in file for match in re.findall(pattern, line)]
    return domains

domains = extract_domains('radio_stations.txt')
for domain in domains:
        print(domain)
