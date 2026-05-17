#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).map { |f, t, fl| "#{f},#{t},#{fl}" }.join
