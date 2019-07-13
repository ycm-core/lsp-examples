class Badger
  
  attr_accessor :name, :size # Creates getter and setter methods.
  
  def initialize(name, size)
    @name = name
    @size = size
  end
  
  # Instance method
  def name_backwards
    @name.reverse
    @name.
  end
  
  #
  def self.
  
end

# Create the new instance.
badger = Badger.new('Charles', 12)

# Access it's attributes.
puts badger.size # => 12
puts badger.name # => Charles
badger.size = 15
puts badger.size # => 15

# OMGWTF open the class up and add new methods.
class Badger
  def double_size
    @size*2
  end
end

puts badger.double_size # => 30

# singleton methods
def badger.moo
  puts "moo"
end

another_badger => Badger.new('Alice', 3)

puts badger.moo # => 'moo'
puts another_badger.moo # => Method Not Found Error
