# -*- mode: ruby -*-
# vi: set ft=ruby :

#----------------------------
# HELPER METHOD
#----------------------------

#

# This does the same as 'kubeadm token generate'
def get_cluster_token()
  token = "#{SecureRandom.hex(3)}.#{SecureRandom.hex(8)}"
  File.write($TOKEN_FILE, token)
token
end


Vagrant.configure("2") do |config|
  # LOGIC FLOW OF THIS SCRIPT - Please adhere to this or change it

  config.vm.define "lin" do |lin|
    lin.vm.box = "hashicorp/bionic64"
    #lin.vm.network "public_network" # just for the task
    lin.vm.network "forwarded_port", guest: 22, host: 2223
    lin.ssh.port = 2223
    lin.vm.box_check_update = false
    lin.vm.synced_folder ".", "vagrant", disabled: true
    lin.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2
    apt-get install -y software-properties-common
    apt-add-repository --yes --update ppa:ansible/ansible
    apt-get install -y ansible
    ansible --version
    SHELL
  end

  config.vm.define "win" do |win|
    win.vm.box = "gusztavvargadr/windows-10"
    win.vm.network "public_network" # just for the task
    win.vm.network "forwarded_port", guest: 80, host: 8082, host_ip: "127.0.0.1"
    win.vm.box_check_update = false
  end

  config.vm.define "win" do |centos|
    centos.vm.box = "centos/7"
    centos.vm.network "public_network" # just for the task
    centos.vm.network "forwarded_port", guest: 80, host: 8081, host_ip: "127.0.0.1"
    centos.vm.box_check_update = false
  end
  
end

