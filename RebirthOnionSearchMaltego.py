import requests
import re
import urllib.parse
import subprocess
from bs4 import BeautifulSoup
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
import html
import urllib3

class RebirthOnionSearchMaltego(DiscoverableTransform):

    def get_title(url):
        session = requests.session()

        proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
        }

        session.proxies = proxies

        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.title.string

    def search_links(name):
        final_all_cleaned_list = []
        session = requests.session()

        proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
        }

        session.proxies = proxies

        url = f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={name}"
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        anchor_list_ahmia = [anchors_tags['href'] for anchors_tags in soup.find_all("a")]

        cleaned_link_ahmia = f'/search/search/redirect?search_term={name}&redirect_url='
        cleaned_list_1_ahmia = [link_ahmia.replace(cleaned_link_ahmia, '') for link_ahmia in anchor_list_ahmia[12:21]]

        for cleaned_link_2_ahmia in cleaned_list_1_ahmia:
            cmd = f'curl -o /dev/null -s -w "%{{http_code}}\\n" --socks5-hostname localhost:9050 {cleaned_link_2_ahmia}'
            try:
                status = str(subprocess.check_output(cmd, shell=True))
                if status == "b'200\\n'":
                    final_all_cleaned_list.append(cleaned_link_2_ahmia)
            except:
                pass

        # Haystack Scraper
        url = f"http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q={name}"
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        anchor_list_haystack = [anchors_tags['href'] for anchors_tags in soup.find_all("a", href=re.compile("^redir\.php\?url="))]

        cleaned_list_1_haystack = [urllib.parse.unquote(link.replace('redir.php?url=', '')) for link in anchor_list_haystack[:11]]

        for cleaned_link_2_haystack in cleaned_list_1_haystack:
            cmd = f'curl -o /dev/null -s -w "%{{http_code}}\\n" --socks5-hostname localhost:9050 {cleaned_link_2_haystack}'
            try:
                status = str(subprocess.check_output(cmd, shell=True))
                if status == "b'200\\n'":
                    final_all_cleaned_list.append(cleaned_link_2_haystack)
            except:
                pass

        # Haystack Tormax
        url = f"http://o2yumlw2lxbwdtz6ph5beve7celspvf4suqmb3wf5thfjsn7d47wz6ad.onion/search?T={name}"
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        anchor_list_haystack = [anchors_tags['href'] for anchors_tags in soup.select("a.navbar-brand, a.nav-link, a.w-100, a.text-dark, a.px-2, a.text-decoration-none")]

        all_links = []
        for link in anchor_list_haystack[:10]:
            cmd = f'curl -o /dev/null -s -w "%{{http_code}}\\n" --socks5-hostname localhost:9050 {link}'
            status = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
            if status == "200":
                all_links.append(link)

        return all_links

        return final_all_cleaned_list

    @classmethod
    def create_entities(cls, request, response):
        research = request.Value
        try:
            searching = cls.search_links(research)
            if searching:
                for i, result in enumerate(searching, start=1):
                    title = cls.get_title(result)
                    entity = response.addEntity('maltego.Banner', title)
                    entity.addProperty(f'LinkNumber{i}', displayName="Address .onion", value=result)
            else:
                response.addUIMessage("No result : ", messageType=UIM_PARTIAL)
        except IOError:
            response.addUIMessage("An error has occurred : ", messageType=UIM_PARTIAL)


if __name__ == '__main__':
    RebirthOnionSearchMaltego.searchLink("computer")
