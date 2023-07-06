#!/usr/bin/env ruby
# script that outputs sender phone or name, reciever data and flags
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join
