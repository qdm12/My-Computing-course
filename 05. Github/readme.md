# 5. Github

[![Github][github_image]][github_link]

## What is it used for?
- Code history
- Code backup
- Collaborative coding
- "*Open source*"
- See later: Testing, deployment, Slack etc.

## Github account and Git
1. Create an account on [**Github**][github_link]
2. Download and install [**Git**][git_link]

## Create your *repository* on Github
1. Go to [**github.com/new**](https://www.github.com/new)
2. Enter the repository name "first-project" and click **Create repository**
3. If your username is *ddenise*, copy your repository Git link https://github.com/ddenise/first-project.git

## **Clone** your repository
- In your terminal, enter `git clone https://github.com/ddenise/first-project.git` :arrow_double_down:
- On Mac OSX, you will have to install Xcode which will automatically be prompted to you.

## Modify your *local* repository
5. Enter `cd first-project` :open_file_folder:
6. Enter `touch readme.md` :new: and open this new file with a text editor or Liclipse
7. Copy and paste this into *readme.md* (*.md* stands for **Markdown**):
```
# first-project

## What is this?
This is my first project to understand the basics of *Git* and *Github*

## What was **learnt**?
- `git clone` :arrow_double_down:
- `git add`
- `git commit -m "message"`
- `git push` :arrow_up:
- `git pull` :arrow_down:
- `git push -b existing-branch`
- `git checkout -b new-branch`
- `git checkout existing-branch`

:clap:
```

## Add and upload your changes to Github
8. In your terminal, enter `git add readme.md`
9. Enter `git commit -m "Added the readme file"`
10. Enter `git push` :arrow_up: (*this uploads your changes to Github*)
11. Go to [github.com/**ddenise**/first-project](https://www.github.com/ddenise/first-project). 
    There is now one file named *readme.md* and, as you can see, 
    it is displayed nicely if you scroll down :open_mouth:

## How someone else working on this code could affect you
### Modify directly on Github (*we don't usually do that, except for README.md*)
1. On your *first-project* Github webpage, click on **readme.md**
2. Click on the pencil :pencil2: on the top right corner to edit the file
3. Change something and click **Commit changes**

### Update your local repository
4. Back on your computer's terminal, your *local* repository is now **outdated**
5. To update it with your changes made on Github, enter `git pull`
6. This works the same when someone else works on the code and you want to get his or her changes
7. If you overthink that, don't worry we use things called *branches* to avoid conflicts etc.

## Time to be useful

### Copy what we have done so far
- We assume `path1/myproject` is the path to your Liclipse project and `path2/first-project` is the path to the Github repository
- Open your terminal
    - `cp -r path2/first-project/* path1/myproject/` to copy the `.git` folder and *readme.md* file to your Liclipse project.
    - The `*` means **anything** so will match any files/folders in *first-project*.

### Check what's up with Git
- In your terminal, `cd path1/myproject`
- Enter `git status` and it will show you the few files not registered in **red**.
- We want them to be **green** except some of them actually...

### Ignore some files for Git
- We don't want these files on Github:
    - The project files *.project* and *.pydevproject* are only required by Liclipse.
    - The *.pyc* files are only used to run the code, and are not necessary.
- The solution
    - Create a file *.gitignore* and write that into it:
    ```
    .project
    .pydevproject
    *.pyc
    ```
- Enter `git status` again, and these files will disappear from git :wink:
- Why: because later on you might use `git add .` to add all the modifications made in all the files

### Finally updating Github
1. Enter `git add .` to add all the files you modified
2. Check with `git status` that's what you want (*should* be)
3. Enter `git commit -m "Added my first Python code I've made"`
4. Enter `git push` :arrow_up: ... **DONE**
5. You can check on your Github webpage that your additions are there.

## One last minute addition
- Now that you master a few commands and the concept of Git...
- Just install [**GitKraken**][gitkraken_link] and set it up somehow for your repository
- It's basically the same as before except it looks great and you understand what the hell is going on

Time to make some more real-life-like [Python code with Excel][lesson_06] :snake:

## What did you learn?
- Basic use of Git and Github
- Markdown for `readme.md` in Github
- Quick preview of collaborative coding in Github
- GitKraken.. that you will use soon

## To add to your resume
- Git
- Github
- Markdown
- GitKraken
  
[github_image]: /internals/icons/github.png
[github_link]: https://www.github.com/join
[git_link]: https://www.git-scm.com/downloads
[gitkraken_link]: https://www.gitkraken.com/download
[lesson_06]: /06.%20Python%20and%20Excel
