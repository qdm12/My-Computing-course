# 3. Vagrant

[![Vagrant][vagrant_image]][vagrant_link]

## Abreviations
- OS: Operating system
- VM: Virtual machine (guest OS running on your host OS)
- `cd`: Change directory command :open_file_folder:

## Install ssh (*secure shell*)
- On *Mac* and *Linux*: it's already here :smile:
- On *Windows* :scream:
  1. Download and install [**Git**][git_link] :octocat:
  2. In the Windows search bar, paste **edit the system environment variables** and open it
  3. Click on **Environment variables...** (bottom)
  4. In the *System variables* section, search for the variable **Path** and select it
  5. Click on **Edit...**
  6. If on Windows 10, click on **Edit text...**
  7. Add `;C:\Program Files\Git\usr\bin` to the end of the text and press OK to close all windows. :+1:

## Install Vagrant
1. Download and install [**Virtual Box**][virtualbox_link]
2. Download and install [**Vagrant**][vagrant_link]
3. **ONLY** IF YOU ENCOUNTER PROBLEMS LATER, check the [Hardware Virtualization Stuff](#Hardware%20Virtualization%20Stuff)

## Vagrantfile and simplest Vagrant VM
1. Launch your terminal (*Terminal* or *cmd.exe*) :black_small_square:
2. Enter `mkdir NewDirectory && cd NewDirectory` :new:
3. Enter `touch Vagrantfile` to create a new file called *Vagrantfile* :new:
4. Open this *Vagrantfile* with your code editor (You can try with `atom Vagrantfile`) 
5. Copy this into it and save it:
  ```Ruby
  Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
  end
  ```
6. Back to your terminal, enter **`vagrant up`** :sparkles:
  - This setup up the VM according to your *Vagrantfile*
  - It will show a lot of BS you don't need to know about
  - It will take some time :hourglass: to download *trusty64* the first time only
7. Enter `vagrant ssh` to log in the VM.
8. In the VM (you are here), enter `cd /vagrant`
9. In the VM, enter `ls` - That's the **shared** directory
10. In the VM, enter `exit` to go back to your host OS's terminal
11. Enter `vagrant halt` to shutdown the VM.
12. And/Or enter `vagrant destroy` to delete it completely.

## Probems before Vagrant
- It only works on my machine :poop:
- OS compatibility issues, "Portability" :-1:
- You don't remember how you made it work on your computer :-1:
- Your program and environment should be like :sheep:, not like your :poodle:

## Advantages
- Creates an *environment* defined in the **Vagrantfile**
  - Specific OS (*ubuntu server* aka trusty64)
  - The *host OS*'s directory from where Vagrant is launched is shared at `/vagrant`.
  - Specific applications (*git*, *python*, ...)
  - Specific networking, CPUs, RAM
- The **disposable** operating system (OS)
  - Vagrant provide a disposable *OS* running in your computer's OS.
  - Your OS is not modified
  - You can just *throw it away* and *re-create it*
- Anyone can use it without knowing what is actually needed
- Serves as a blueprint of what steps were taken to setup the environment for your program
- You can easily re-produce the steps to deploy it to the cloud etc.

## More complete Vagrantfile (the initial one used in this project)
```Ruby
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
Explanations:
- `vb.memory = "512"` sets the VM to use 512 MB of your RAM
- `vb.cpus = "1"` sets the VM to use 1 of your CPU cores
- `vb.name = "Vagrant-virtual-machine"` sets the name of your VM
- `config.vm.hostname = "denisa"` sets the VM's username
- `config.vm.box = "ubuntu/trusty64"` sets the VM's OS to use which is downloaded only once
- `config.vm.provision "shell", inline: <<-SHELL` tells `vagrant up` to launch the terminal of the new VM
- `sudo apt-get install git` installs git on the VM for example
- The rest will be explained later

# Essential to remember
- **Vagrantfile** to describe VM :memo:
- **`vagrant up`** to create or start the VM :rocket:
- **`vagrant halt`** to shutdown the VM :zzz:
- **`vagrant destroy`** to destroy the VM :boom:
- In the VM, the directory **`/vagrant`** is the shared directory :file_folder:
- We will see in [lesson 05][lesson_05]: **`vagrant provision`** (update the running VM)

Time to see how to make use of [git and Github][lesson_04]

### Hardware Virtualization Stuff :rotating_light:
- Check your *Hardware Virtualization* is ON in your BIOS
  1. Reboot computer
  2. Press on DEL (or F2, F10, F12) several times when it starts booting
  3. Search for the hardware virtualization option in the BIOS and turn it on
- If you don't have VT-x / VMX/ AMD-x available do the following
  1. Replace *trusty64* by *trusty32* in the Vagrantfile
  2. Set `vb.cpus = 1` in the Vagrantfile


[vagrant_image]: /internals/icons/vagrant.png
[vagrant_link]: https://www.vagrantup.com/downloads.html
[git_link]: https://www.git-scm.com/downloads
[virtualbox_link]: https://www.virtualbox.org/wiki/Downloads
[lesson_04]: /04.%20Github
[lesson_05]: /05.%20Excel%20file%20and%20data