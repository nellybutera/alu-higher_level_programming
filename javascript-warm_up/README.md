### This a Javascript Project completing different tasks to accurately grasps concepts about Jquery and other simple javascript scripts.


#### Fixes for some problems i run into

```bash
- added a workspace settings to add LF Line Endings in my files
- ran github command "git config core.fileMode true" to stop github from changing my files permissions
```

### To change all file permission at the same time you can run:

```bash
find . -type f -name "*.js" -exec git update-index --chmod=+x {} \;

```