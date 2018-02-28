# Nganu Number

tau lupa dah, tapi ini test pertama sebelum `flask-post-api`

Python :

```python
buf = 1
for i in range(1,100):
    buf = i * buf

print ">" + str(buf) # + 0

bufstr = str(buf)
buflen = len(bufstr)
result = 0

for i in range(0, int(buflen)):
    if i == 0:
        result = i
    else:
        split = int(bufstr[i])
        assign = result + split
        result = assign

print result

```

Ruby :

```ruby
buf = 1
(1..100).each { |i| buf = i == 1 ? i : i * buf }
puts buf

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
```

Result :

```shell
# Ruby
ruby@ayam:~/Documents/test$ ruby number.rb
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
648
# Python
ruby@ayam:~/Documents/test$ python number.py
>933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000
639
```