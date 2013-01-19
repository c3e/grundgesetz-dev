#/usr/bin/env ruby

require "fileutils"

patches = 2..59

patches.each {|i|
  dir_n = i.to_s
  Dir.mkdir dir_n
  if i > 1 then
    prev_dir_n = (i-1).to_s
    Dir.foreach(prev_dir_n){ |f|
      next if /^\.+/ =~ f
      FileUtils.cp(File.join(prev_dir_n, f), File.join(dir_n, f))
    }
    `patch -d #{dir_n} -p1 < patches/#{dir_n}`
  end
}
