buf = 1
(1..100).each { |i| buf = i == 1 ? i : i * buf }

bufstr = buf.to_s
buflen = buf.to_s.size
result = 0

(0...buflen).each do |i|
  result = bufstr[i].to_i if i == 0 #
  if i > 0
    split = bufstr[i].to_i
    assign = result + split
    result = assign
  end
end

puts result
