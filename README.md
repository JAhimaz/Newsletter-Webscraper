# Newsletter-Webscraper

![Project Status](https://img.shields.io/badge/Project%20Status-Ongoing-orange?style=for-the-badge&logo=github)

Scrapes through websites to detect whether or not they have a newsletter within their website. Utilises Python libraries such as BeautifulSoup4 and Requests-HTML 

Results will be provided in a CSV format, with the time taken to scrape each site.

Example Results:

| URL  | Has Newsletter | Time Taken
| ------------- | ------------- | ------------- |
| https://joshuaahimaz.com | No | 3.208212 |
| https://source-forum.com/ | Yes | 3.600061 |
| https://plusthis.com/ | No | 7.821983 |

Enter URLS in `urls.txt`

```python
https://example.com
https://thisisanotherexample.com
https://mywebsite.com
```

### Previews

![preview](https://github.com/JAhimaz/Newsletter-Webscraper/blob/main/previews/preview.gif)


### Libraries Used

[requests==2.27.1](https://pypi.org/project/requests/)

[requests-html==0.10.0](https://pypi.org/project/requests-html/)

[beautifulsoup4==4.10.0](https://pypi.org/project/beautifulsoup4/)


