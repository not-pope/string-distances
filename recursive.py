#this one gets slow reaaaaallllllyyyy fast

def lev_recursive(a,b):
  i=len(a)
  j=len(b)
  if i==0:
    return j
  if j==0:
    return i

  flagy=1 if a[0]!=b[0] else 0
  
  return min(
    lev_recursive(a[1:],b)+1,
    lev_recursive(a,b[1:])+1,
    lev_recursive(a[1:],b[1:])+flagy
  )

print(lev_recursive('kitten','sitting'))
print(lev_recursive('systems','applications'))