#  sougou weinxin articles crawler
 
 a crawler that can download articles from a given weixin official account

## background knowledge:

###what happens when you type an url in the browser and press enter?
 1. through the domain name find the ip address
     + either from cache or from DNS server   
 2. Browser initiates a TCP connection with the server
 3. The browser sends an HTTP request to the web server.
    + GET request for asking web page
    + POST request for summit some info to the server
    + may have many other requests
 4. The server handles the request and sends back a response.Then the server sends out an HTTP response.
    * 1xx indicates an informational message only
    * 2xx indicates success of some kind
    * 3xx redirects the client to another URL
    * 4xx indicates an error on the client’s part
    * 5xx indicates an error on the server’s part 
 5. The browser displays the HTML content (for HTML responses which is the most common).
 
 ## How the crawler works?
 Crawler, Spider, Robot, SearchBot whatever you call it, is a program that is able to ..
 crawl through a given website and scrape out some desired data. google search engine is 
 actually a crawler called GoogleBot. 
 
 In our simple python project, we followed these steps:
 1. request the html based on the given keywords 
    + we need generated the url based on our keywords
    
 2. fetch the html content from that url
     * may need to unblock the restrictions of crawler from the original web   
     in this sogou wechat , we need to unblock it from manually input the validation code
 
 3. parse the needed info from the fetched file 
  