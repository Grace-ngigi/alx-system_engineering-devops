#!/usr/bin/env ruby
#regex matching repetitive token
puts ARGV[0].scan(/hbt{2,5}n/).join
