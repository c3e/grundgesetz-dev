#/usr/bin/env ruby

# run in "src"
# creates subdirectory for every patch (1--59) and applies patches

require "fileutils"

patches = 1..59

patches.each {|i|
  dir_n = i.to_s
  Dir.mkdir dir_n
  if i == 1 then
    prev_dir_n = "."
  else
    prev_dir_n = (i-1).to_s
  end
  Dir.foreach(prev_dir_n){ |f|
    puts f
    next if /^\.+$/ =~ f
    next if /\.md$/ !~ f
    FileUtils.cp(File.join(prev_dir_n, f), File.join(dir_n, f))
  }
  `patch -d #{dir_n} -p1 < patches/#{dir_n}`
}
