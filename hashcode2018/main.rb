#!env ruby

require 'pry'
require 'awesome_print'
require './file_outputer.rb'
require './file_reader.rb'
require './algorithm.rb'

if ARGV[0].nil? || ARGV[0].empty?
  puts 'Please input a valid file as an arguement'
  exit
end

input = FileReader.process_input(ARGV[0])

results = Algorithm.perform(input)

FileOutputer.write(results[:cars], ARGV[0])

puts "Done with #{ARGV[0]}"