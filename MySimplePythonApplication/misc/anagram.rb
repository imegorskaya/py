class Anagram
  # this is an anagram
  def anagram
    chars_size = (chars = self.split('')).size
    return chars if chars_size == 1
    return [chars,chars.reverse] if chars_size == 2
    ret = []; chars.each do |c|
      (temp = chars.clone).delete_at(chars.index(c));
      ret += temp.to_s.anagram.collect{|a| "#{c}#{a}" }
    end
    ret.uniq
    a
  end
end
