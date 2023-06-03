#!/bin/bash
git config --list
git config --global user.name "malihejafari"
git config --global user.email "mlh.jafari86@gmail.com"
token = "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"
username = "malihejafari"
repo = "number-to-words"
git clone https://{token}@github.com/{username}/{repo}
cd {repo}
!cp -r /content/firstprj /content/number-to-words
git status
git add . 
git status
!git commit -m "add number to words project"
git log --oneline
git remote -v
git push https://{token}@github.com/{username}/{repo}
git status