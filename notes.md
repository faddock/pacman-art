```shell
#workflow
rm -rf .git
git init
git remote add origin https://github.com/faddock/pacman-art.git
python3 create-pacman.py
git branch -M main
git push -u origin main
git add .
git commit -m "commit so i can go sleep"
git push 
```

