#Create a file in /tmp

file {'/tmp/school':
	mode => '0744',
	owner => 'www-data',
	content => 'I love Puppet',
	group => 'www-data'
}
