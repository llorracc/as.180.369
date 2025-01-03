reproduce files:
- In your paper directory
- Create a folder: binder
- create the environment file: NOTE update with correct versions of each package
```
conda env export --from-history -f environment.yml
```
- create a reproduce.sh file
- give it permission to be executable
  - ```ls -las``` (shows if it is executable)
  - ```chmod u+x reproduce.sh ```
  - ```/bin/bash reproduce.sh```
