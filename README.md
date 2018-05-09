# dealii-repo-contributors

generate commit/contributor statistics for the deal.II repository

to update:

1. grep authors:
```
   git log --date=short --format="%ad %an %aE" >authors.in
```
2. grep from changelog:
```
    cat /ssd/deal-git/doc/news/changes/*/*>changelog.in
    python changelog.py >from_changelog
```
3. update mapping:
by modifying cleanup.py
...

4. cleanup
```
    cat from_changelog authors.in | python cleanup.py >clean.dat
```
5. by month
```
    cat clean.dat | python bymonth.py | sort >bymonth.dat 
```
6. by quarter:
```
    cat clean.dat | python byquarter.py | sort >byquarter.dat 
```
6. commits by month
```
    git log --date=short --format="%ad %an %aE" | sort >commits.in
    cat commits.in  | python commits.py >commits.dat
```
6. commits by quarter
```
    cat commits.in  | python commits_quarter.py >commits_quarter.dat
```