Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.network "private_network", ip: "192.168.56.10"
    config.vm.hostname = "web-server"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "apache-server"
      vb.memory = "1024"
    end
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y ansible
    SHELL
  end
  