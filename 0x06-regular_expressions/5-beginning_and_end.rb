#!/usr/bin/env ruby
#regex exactly matching a string starting with h and ending with n
puts ARGV[0].scan(/^h.n$/).join
