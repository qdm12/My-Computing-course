# 4. Github

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
6. Enter `touch readme.md` :new: and open this new file with your text editor
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
### Modify directly on Github (*don't do that except for README.md*)
1. On your *first-project* Github webpage, click on **readme.md**
2. Click on the pencil :pencil2: on the top right corner to edit the file
3. Change something and click **Commit changes**

### Update your local repository
4. Back on your computer's terminal, your *local* repository is now **outdated**
5. To update it with your change, enter `git pull`
6. This works the same when someone else works on the code and you want to get his or her changes
7. If you overthink that, don't worry we use things called *branches* to avoid conflicts etc.

## Time to be useful: adding two real files
1. Creating the files on your computer
    1. `cd` to your *first-project*
    2. In the terminal, enter `touch requirements.txt` to create the file *requirements.txt* :new: but put nothing into it
    3. Enter `touch Vagrantfile` to create the file *Vagrantfile* :new:
    4. With your code editor, copy the following in the *Vagrantfile*
    ```ruby
    Vagrant.configure(2) do |config|
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 2
      vb.name = "Vagrant-virtual-machine"
    end
    config.vm.hostname = "denisa"
    config.vm.box = "ubuntu/trusty64"
    config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y git python-pip python-dev
      sudo apt-get -y autoremove
      cd /vagrant
      sudo pip install -r requirements.txt  
    SHELL
    end
    ```
2. Updating Github with your changes
  1. Enter `git add Vagrantfile requirements.txt`
  2. Enter `git commit -m "Added initial Vagrantfile and requirements files"`
  3. Enter `git push` :arrow_up:

## One last minute addition
- Now that you master a few commands and the concept of Git...
- Just install the [**GitKraken**][gitkraken_link] and set it up somehow for your repository
- It's basically the same as before except it looks great and you understand what the hell is going on
  
## More advanced: Probably see that later on :dizzy_face:
- Branches ! But just use GitKraken to check that out, it's way easier to understand !

Time to use your brain and write [Python code][lesson_05] :snake:

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
[lesson_05]: /05.%20Python%20and%20setup
