#Konfiguracja procesu do weryfikacji składni w swoim repozytorium na github, który będzie uruchamiany automatycznie po każdym commicie.

#1
#.github/workflows/

#2
#pep8_check.yml

#3
#pycodestyle --count --statistics --exclude=venv,tests/temp .

#4
#setup.cfg

#5
#git add .github/workflows/pep8_check.yml

#6
#git commit -m "Add PEP8 workflow"

#7
#git push