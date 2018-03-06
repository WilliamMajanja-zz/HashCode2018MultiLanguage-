#!env ruby

class FileOutputer
	def self.write(input, file_name)
    File.open("./#{DateTime.now.to_time.tr(':', '_')}_#{file_name.split(".").first}_result.txt", 'w') do |file|
      input.each do |car|
        file.write "#{car.size} "
        car.each { |ride_num| file.write "#{ride_num} " }
        file.puts ""
      end
		end
	end
end
