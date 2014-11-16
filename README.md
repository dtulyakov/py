# для обучения - python #

```
#!python
# NEW
mkdir /path/to/your/project
cd /path/to/your/project
git init
git remote add origin ssh://git@bitbucket.org/dtulyakov/py.git
 
# NOT NEW
cd /path/to/my/repo
git remote add origin ssh://git@bitbucket.org/dtulyakov/py.git
git push -u origin --all # только в первый раз
git push -u origin --tags # и теги туда же

echo "# This is my README" >> README.md
git add . && git commit -a && git push -u origin master
```
