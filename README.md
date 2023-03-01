# FFID
### A script to fuzz websites for information disclosures.
Latest implementations:
  1.  Implement multithreading to speed up the fuzzing process and increase the number of requests per second.
  2.  Use a smarter wordlist or wordlist generator that includes common file and directory names, as well as different file extensions.
  3.  Implement an option to include common HTTP headers (e.g. User-Agent, Referer, Cookie) in requests to simulate real user traffic.
  4.  Implement an option to use a proxy server to hide the origin IP address and avoid getting blocked by the target server.
### Description:
This script is a Python script that performs fuzzing on a specified URL. Fuzzing is the process of sending a large number of inputs, called "fuzz tests," to a program or system to detect vulnerabilities or errors. The script takes a URL as input and can optionally take a wordlist of directories and files to test, a list of file extensions to test, and options to use headers or a proxy.

The script uses the requests library to make HTTP requests to the specified URL with a GET method. The function check_url checks the response from the server and prints the URL and the size of the response if the response status code is 200 (OK). The fuzz function takes the URL, wordlist, extensions, use_headers, and use_proxy as arguments and calls the functions fuzz_wordlist and fuzz_extensions, passing in the URL and the wordlist or extensions, respectively.

If a wordlist is provided, the script reads in the wordlist and creates ten threads to fuzz the URL with each word in the wordlist. Each thread calls the function fuzz_wordlist, which concatenates the URL with each word in the wordlist and calls check_url with the resulting URL.

If a list of extensions is provided, the script creates a thread for each extension and calls the function fuzz_extensions, which concatenates the URL with the string "test" and each extension in the list and calls check_url with the resulting URL.

Overall, this script can be useful for detecting potential vulnerabilities or hidden files on a web server by sending a large number of requests and checking the responses.
