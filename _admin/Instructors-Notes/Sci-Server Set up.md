**Getting set up for SciServer

1. Create an account with SciServer (using your JHU email address)
- go to Sciserver.org
- navigate to log-in
- create a new account with your JHU email address

2. Create a container
- log in to SciServer
- navigate to 'compute'
- to compute files, we need to create a container in which the files can live.
- click on 'Create container'
- Container name: Class name
- Compute Image: econ-ark (This is important!)
- User volumes: persistent and temporary
- click on create

3. Create files and run your first myst file
- tp start eh new container you have to click on it (it should open jupyerlab directly)
- navigate on the left side to the folder with your User-name
- navigate to 'persistent'
- clone your class repo here (git clone https://......)
- navigate to the folder 'contribute/camriddell' ane explore his files

4. Myst files
- Find the myst documentation page on google
- scroll to the read-me file and have a look at the examples
- try to replicate some of the code in your own jupterlab file.

5. Your class assignment
- For your class assignment make a copy of the folder 'contrib/camriddell/jupyterbook-demo'
- Create your own jupter lab file (.ipynb)
- Write your class assignment

5. Run your jupyer book:
- Install jupterbook doing the following
```
pip install jupyter-book
```
- Navigate to the folder above the jupyerbook on the terminal
- Build your jupter book with the command 
```
jupyter-book build FolderName
```
- Find the newly built jupyer book and open it.
- That's it you have just accomplished to run your own jupter book! Congrats!

NOTE:
- If you run into issues it is very likely that you are not the only one. Therefore, create an issue on the Github page and discuss with your peers and TAs.
