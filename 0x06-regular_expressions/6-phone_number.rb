#!/usr/bin/env ruby
#This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.
#
#Requirement:
#
#The regular expression must match a 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/)
