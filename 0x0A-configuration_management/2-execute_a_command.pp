# This Puppet Manifest kills a process name 'killmenow'

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
}
