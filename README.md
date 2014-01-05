NEW
mkdir /path/to/your/project
cd /path/to/your/project
git init
git remote add origin ssh://git@bitbucket.org/dtulyakov/py.git

NOT NEW
cd /path/to/my/repo
git remote add origin ssh://git@bitbucket.org/dtulyakov/py.git
git push -u origin --all # pushes up the repo and its refs for the first time
git push -u origin --tags # pushes up any tags


echo "# This is my README" >> README.md
git add README.md
git commit -m "First commit. Adding a README."
git push -u origin master

