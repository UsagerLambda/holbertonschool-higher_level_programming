#!/usr/bin/env python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        data = r.json()
        for post in data:
            print("{}".format(post['title']))
    else:
        print("Une erreur est survenue : {}".format(r.status_code))


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = []
        data = r.json()
        for post in data:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts.append(post_dict)
        with open('posts.csv', 'w') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
    else:
        print("Une erreur est survenue : {}".format(r.status_code))
