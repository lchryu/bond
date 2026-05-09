cur = 1339
end = 222
while True:
    
    h = cur // 60
    m = cur % 60
    
    t = t + cnt(h, m)
    
    if cur == end: break
    
    cur = (cur + 1) % 1440
    
    
    