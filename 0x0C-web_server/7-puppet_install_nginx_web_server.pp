# This Puppet manifest installs and configures a Nginx server

package { 'nginx':
    ensure => installed,
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '
        server {
            listen 80 default_server;
            listen [::]:80 default_server;

            location / {
                root /var/www/html;
                index index.html index.htm index.nginx-debian.html;
            }

            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }
        }
    ',
    notify  => Service['nginx'],
}
