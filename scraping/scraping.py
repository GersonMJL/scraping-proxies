import requests
import re
import time
from bs4 import BeautifulSoup
from urllib.parse import unquote


def ip_regex(tag_ip: str):
    """Regex to find IP address inside HTML tag

    Args:
        ip (str): HTML tag with IP address

    Returns:
        str: IP address
    """
    regex = r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b"
    search = re.search(regex, tag_ip)
    return search.group()


def get_proxies():
    """Scrap all proxies from https://free-proxy-list.net/

    Returns:
        list: List of proxies
    """
    source = "https://www.freeproxylists.net/"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Origin": "https://www.freeproxylists.net",
        "Host": "www.freeproxylists.net",
        "Cookie": "hl=en",
        "Referer": "https://www.freeproxylists.net/",
        "content-type": "application/x-www-form-urlencoded",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    proxies = []

    s = requests.Session()
    s.headers.update(head)

    r = s.get(source)

    s.cookies["pv"] = "20"
    s.cookies["from"] = "direct"
    s.cookies["userno"] = "20220227-002452"
    s.cookies["hl"] = "en"
    s.cookies["visited"] = "2022%2F02%2F27%2007%3A55%3A03"

    soup = BeautifulSoup(r.text, "html.parser")

    div_page = soup.find("div", {"class": "page"})
    number_of_pages = div_page.findAll("a")
    number_of_pages = len(number_of_pages)

    table = soup.find("table", {"class": "DataGrid"})
    all_tr = table.find_all("tr", {"class": ["Odd", "Even"]})

    i = 1
    j = 1

    while j <= number_of_pages:
        time.sleep(2)
        r = s.get(source + "?page=" + str(j))
        soup = BeautifulSoup(r.text, "html.parser")
        j += 1

        for i in range(len(all_tr)):
            proxie_list = []
            proxie = {
                "ip": "",
                "port": "",
                "protocol": "",
                "anonymity": "",
                "country": "",
                "region": "",
                "city": "",
                "uptime": "",
                "uptime": "",
                "response": "",
                "transfer": "",
            }
            row = table.findAll("tr")[i :: i + 1]
            all_td = row[0].find_all("td")
            if len(all_td) < 10:
                i += 1
                continue
            else:
                for td in all_td:
                    script_tag = td.find("script")
                    bar = td.find("span", {"class": "bar"})
                    if script_tag:
                        ip_encoded = script_tag.text
                        # regex to match everything inside the quotes
                        ip_encoded = re.search(r'"(.*?)"', ip_encoded).group(1)
                        ip = unquote(ip_encoded)
                        proxie_list.append(ip_regex(ip))
                    elif bar:
                        width = bar.get("style").split("width:")[1].split(";")[0]
                        proxie_list.append(width)
                    elif td.text == "":
                        proxie_list.append("None")
                    else:
                        proxie_list.append(td.text)

                proxie["ip"] = proxie_list[0]
                proxie["port"] = proxie_list[1]
                proxie["protocol"] = proxie_list[2]
                proxie["anonymity"] = proxie_list[3]
                proxie["country"] = proxie_list[4]
                proxie["region"] = proxie_list[5]
                proxie["city"] = proxie_list[6]
                proxie["uptime"] = proxie_list[7]
                proxie["response"] = proxie_list[8]
                proxie["transfer"] = proxie_list[9]

                # print("\n")
                # print(proxie)
                proxies.append(proxie)

            i += 1

    return proxies
