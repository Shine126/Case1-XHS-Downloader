from requests import get


class Html:

    def __init__(
            self,
            headers: dict,
            proxies=None,
            timeout=10, ):
        self.headers = headers
        self.proxies = {
            "http": proxies,
            "https": proxies,
            "ftp": proxies,
        }
        self.timeout = timeout

    def get_html(
            self,
            url: str,
            params=None,
            headers=None, ) -> str:
        try:
            response = get(
                url,
                params=params,
                proxies=self.proxies,
                timeout=self.timeout,
                headers=headers or self.headers, )
        except (
                requests.exceptions.ProxyError,
                requests.exceptions.SSLError,
                requests.exceptions.ChunkedEncodingError,
                requests.exceptions.ConnectionError,
                requests.ReadTimeout,
        ):
            print("获取网页源码失败！")
            return ""
        return response.text
