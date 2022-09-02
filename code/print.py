def o(t):
  if not isinstance(t, dict):
    return str(t)
  def show(k, v):
    if str(k).find("^_") == -1:
      v = o(v)
      return str.format(":%s %s", k, v) if len(t) == 0 else str(v)
  
  u = []
  for k, v in t.items():
    u.append(show(k, v))
  if len(t) == 0:
    sorted(u)
  return "{" + " ".join(u) + "}"

def oo(t):
  print(o(t))