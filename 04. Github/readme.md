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
2. Enter the repository name "christmas-project" :santa: and **Create repository**
3. If your username is *denisa*, copy your repository link https://github.com/denisa/christmas-project.git

## **Clone** your repository
4. In your terminal, enter `git clone https://github.com/denisa/christmas-project.git`

## Modify your **local** repository
5. Enter `cd christmas-project` :open_file_folder:
6. Enter `touch readme.md` and open this new file with your text editor :new:
7. Copy and paste this into *readme.md*:
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
8. In your terminal, enter `git add readme.md`
9. Enter `git commit -m "Added the readme file about this project"`
10. Enter `git push`
11. Go to [github.com/**denisa**/christmas-project](https://www.github.com/denisa/christmas-project). 
    There is now one file *readme.md* and as you can see it is displayed nicely below :open_mouth:

## How someone else working on this code could affect you
### Modify directly on Github (*don't do that except for README.md*)
1. On your christmas-project Github webpage, click on **readme.md**
2. Click on the pencil :pencil2: on the top right corner to edit the file
3. Change something and click on **Commit changes**

### Update your local repository
4. Back on your computer's terminal, your *local* repository is now outdated
5. To update it with your change, enter `git pull`
6. This works the same when someone else works on the code and you want to get his or her changes

## Time to be useful: adding two real files
1. Creating the files on your computer
  1. `cd` to your *christmas-project*
  2. Enter `touch Vagrantfile` to create the file *Vagrantfile* :new:
  3. With your code editor, copy the following in the *Vagrantfile*
  ```ruby
  Vagrant.configure(2) do |config|
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
      vb.name = "Vagrant-virtual-machine"
    end
    config.vm.hostname = "denisa"
    config.vm.box = "ubuntu/trusty64"
    config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y git 
      sudo apt-get install -y python-pip python-dev
      sudo apt-get -y autoremove
      cd /vagrant
      sudo pip install -r requirements.txt  
    SHELL
  end
  ```
  4. In the terminal, enter `touch requirements.txt` to create the file *requirements.txt* :new:
2. Updating Github with your changes
  1. Enter `git add Vagrantfile requirements.txt`
  2. Enter `git commit -m "Added initial Vagrantfile and requirements files"`
  3. Enter `git push`
  

Time to use your brain and write [Python code][lesson_05] :snake:
  
## More advanced: Probably see that later on :dizzy_face:
- Branches
  - `git checkout -b new-branch` to create a new branch`
  - `git push -b new-branch` to push your changes to the branch "new-branch" created
  - You then have to merge it in the **master** branch through Github.
  - To change back to a branch, enter `git checkout myBranch`
  
[github_image]: /internals/icons/github.png
[github_link]: https://www.github.com/join
[git_link]: https://www.git-scm.com/downloads
[lesson_05]: /05.%20Python