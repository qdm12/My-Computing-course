# 04. Github

[![Github][github_image]][github_link]

## What is it used for?
- Code history
- Code backup
- Collaborative coding
- "*Open source*"
- See later: Testing, deployment, Slack etc.

## Github account and Git
- Create an account on [**Github**](github.com/join)
- Download and install [**Git**](git-scm.com/downloads)

## Create your *repository* on Github
- Go to [**github.com/new**](github.com/new)
- Enter the repository name "christmas-project" :santa: and **Create repository**
- If your username is *denisa*, copy your repository link https://github.com/denisa/christmas-project.git

## **Clone** your repository
- In your terminal, enter `git clone https://github.com/denisa/christmas-project.git`

## Modify your **local** repository
- Enter `cd christmas-project` :open_file_folder:
- Enter `touch readme.md` and open this new file with your text editor.
- Copy and paste this into *readme.md*:
```
# christmas-project

## What is this?
This is my christmas project to understand the basics of *Git* and *Github*

## What was **learnt**?
- `git clone`
- `git add`
- `git commit -m "message"`
- `git push`
- `git pull`
- `git push -b existing-branch`
- `git checkout -b new-branch`
- `git checkout existing-branch`

:clap:
```

## Add and upload your changes to Github
- In your terminal, enter `git add readme.md`
- Enter `git commit -m "Added the readme file about this project"
- Enter `git push`
- Go to [github.com/**denisa**/christmas-project](github.com/denisa/christmas-project)
- There is now one file *readme.md* and as you can see it is displayed nicely :open_mouth:

## Modify directly on Github
- On your christmas-project Github page, click on **readme.md**
- Click on the pencil :pencil2: on the top right corner to edit the file
- Change something and click on **Commit changes**

## Update your local repository
- Back on your computer's terminal, your *local* repository is now outdated
- To update it with your change, enter `git pull`
- This works the same when someone else works on the code and you want to get his or her changes

## More advanced: Probably see that later on :dizzy_face:
- Branches
  - `git checkout -b new-branch` to create a new branch`
  - `git push -b new-branch` to push your changes to the branch "new-branch" created
  - You then have to merge it in the **master** branch through Github.
  - To change back to a branch, enter `git checkout myBranch`
  
[github_image]: /internals/icons/github.png =300x
[github_link]: github.com/join