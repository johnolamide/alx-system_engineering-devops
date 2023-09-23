# This Puppet manifest configures ssh configuration file

#file { '~/.ssh/config':
#  ensure  => file,
#  owner   => 'ubuntu',
#  group   => 'ubuntu',
#  mode    => '0600',
#  content => "
#    Host *
#      IdentifyFile ~/.ssh/school
#      PasswordAuthentication no
#  ",
#}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

