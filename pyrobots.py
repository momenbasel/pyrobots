#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import webbrowser
import re

#banner
print("""
#     ▄███████▄ ▄██   ▄      ▄████████  ▄██████▄  ▀█████████▄   ▄██████▄      ███        ▄████████
#    ███    ███ ███   ██▄   ███    ███ ███    ███   ███    ███ ███    ███ ▀█████████▄   ███    ███
#    ███    ███ ███▄▄▄███   ███    ███ ███    ███   ███    ███ ███    ███    ▀███▀▀██   ███    █▀
#    ███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄██▀  ███    ███     ███   ▀   ███
#  ▀█████████▀  ▄██   ███ ▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀██▄  ███    ███     ███     ▀███████████
#    ███        ███   ███ ▀███████████ ███    ███   ███    ██▄ ███    ███     ███              ███
#    ███        ███   ███   ███    ███ ███    ███   ███    ███ ███    ███     ███        ▄█    ███
#   ▄████▀       ▀█████▀    ███    ███  ▀██████▀  ▄█████████▀   ▀██████▀     ▄████▀    ▄████████▀
#                           ███    ███


#                               @momenbassel
""")



website=input('Enter the domain(with http/s): ')


#checking for input
if not (website[0:4] == "http" or website[0:5] == "https"):
    print("please enter the protocol! (http://example.com)")
    website=input('enter the domain(with http/s): ')
if "robots.txt" in website:
    print("Paths are not allowed, just enter the domain/subdomain only.")
    website=input('enter the domain(with http/s): ')


with urllib.request.urlopen(website+"/robots.txt") as result:
    output = result.read().decode('utf-8')
    if output:
        page =output


def confirm():
    """
    asking for opening robots file endpoints in browser
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("OK to open endpoints at the browser [Y/N]? ").lower()
    return answer == "y"





paths = re.findall("\/\/?.*", page) #regex for finding paths

if paths:
    if confirm():
        for path in paths:
            print(website+path)
            webbrowser.open_new_tab(website+path)
    else:
        for path in paths:
            print(website+path)
