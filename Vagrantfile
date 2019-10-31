Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.raw_arguments =  Shellwords.shellsplit(ENV['ANSIBLE_ARGS']) if ENV['ANSIBLE_ARGS']
  end

  #config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 5000, host: 5000
end
