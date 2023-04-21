# Using Puppet, create a manifest that kills a process named killmenow.
#
# Requirements:
#
# Must use the exec Puppet resource
# Must use pkill

exec { 'end':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin']
  }
