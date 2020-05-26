# frozen_string_literal: true

puts 'Word please: '
text = gets.chomp.downcase
puts 'Number please: '
n = gets.chomp.to_i
puts 'mode pleas: E or D '
mode = gets.chomp.downcase

@n = mode.eql?('e') ? n : n * -1

def decode_or_encode(text)
  alphabet = ('a'..'z').to_a
  key = Hash[alphabet.zip(alphabet.rotate(@n))]
  text.each_char.inject('') { |newtext, char| newtext + (key[char].nil? ? char : key[char]) }
end

puts decode_or_encode(text)
